#!/usr/bin/env python3
"""
Skill Collection Script
Collects skills from multiple sources and organizes them by category.
"""

import os
import shutil
import json
import re
from pathlib import Path
from typing import Dict, List, Set

# Base paths
BASE_DIR = Path("/Users/merlin/Dev/ai-claude-skills-collection")
ECOSYSTEM_DIR = Path("/Users/merlin/Dev/ai-workspace/cloned-repos/claude-ecosystem")
LOCAL_SKILLS = Path("/Users/merlin/.claude/skills")
LOCAL_COMMANDS = Path("/Users/merlin/.claude/commands")
AILABS_DIR = Path("/tmp/ailabs-skills/packages/skills") if Path("/tmp/ailabs-skills/packages/skills").exists() else Path("/tmp/ailabs-skills/dist/skills")
PLUGINS_DIR = Path("/Users/merlin/.claude/plugins/marketplaces")

# Category mappings - keywords to category
CATEGORY_KEYWORDS = {
    "development": [
        "code", "architect", "backend", "frontend", "fullstack", "review", "test",
        "debug", "qa", "security", "secops", "developer", "engineer", "programming",
        "refactor", "lint", "typescript", "javascript", "python", "rust", "go",
        "java", "csharp", "swift", "kotlin", "ruby", "php", "sql", "git", "worktree",
        "tdd", "bdd", "unit-test", "integration", "e2e", "senior-", "code-reviewer"
    ],
    "scientific": [
        "pandas", "numpy", "scipy", "matplotlib", "plotly", "seaborn", "sklearn",
        "scikit", "pytorch", "tensorflow", "keras", "bio", "chem", "rdkit", "protein",
        "genome", "molecular", "physics", "math", "statistics", "polars", "dask",
        "anndata", "scanpy", "deepchem", "alphafold", "pubmed", "uniprot", "chembl",
        "fda", "clinical", "medical", "research", "paper", "scientific", "analysis",
        "visualization", "data-analysis", "statistical"
    ],
    "documents": [
        "pdf", "docx", "xlsx", "pptx", "word", "excel", "powerpoint", "document",
        "markdown", "epub", "notion-export", "csv"
    ],
    "content": [
        "seo", "content", "writer", "copywriting", "blog", "article", "social-media",
        "marketing", "brand", "newsletter", "email-", "pitch", "storytell", "script"
    ],
    "business": [
        "product", "manager", "ceo", "cto", "cfo", "advisor", "strategy", "startup",
        "business", "agile", "scrum", "pm", "owner", "stakeholder", "okr", "kpi",
        "finance", "budget", "revenue", "growth", "investor", "pitch-deck", "validator",
        "regulatory", "compliance", "gdpr", "iso", "fda-", "quality", "audit"
    ],
    "devops": [
        "docker", "kubernetes", "k8s", "cicd", "pipeline", "deploy", "aws", "azure",
        "gcp", "cloud", "terraform", "ansible", "jenkins", "github-actions", "infra",
        "monitoring", "logging", "helm", "container", "serverless", "lambda"
    ],
    "ai-ml": [
        "prompt", "llm", "gpt", "claude", "openai", "anthropic", "langchain", "agent",
        "rag", "embedding", "vector", "transformer", "nlp", "chatbot", "assistant",
        "fine-tune", "lora", "qlora", "ml-engineer", "computer-vision", "huggingface"
    ],
    "automation": [
        "n8n", "mcp", "playwright", "puppeteer", "selenium", "browser", "scrape",
        "zapier", "make", "automate", "workflow", "integration", "api", "webhook",
        "notebooklm", "youtube-transcript", "article-extractor", "tapestry"
    ],
    "meta": [
        "brainstorm", "plan", "skill-creator", "template", "thinking", "problem",
        "decompos", "ultrathink", "validation", "framework", "superpowers", "writing-",
        "receiving-", "requesting-", "finishing-", "executing-", "dispatching-",
        "condition-", "defense-", "root-cause", "sharing-", "testing-skill", "using-"
    ]
}

# Sensitive patterns to exclude
SENSITIVE_PATTERNS = [
    r"auth_info\.json",
    r"library\.json",
    r"credentials\.json",
    r"browser_state",
    r"\.env$",
    r"\.key$",
    r"\.pem$",
    r"secrets\.json",
    r"node_modules",
    r"__pycache__",
    r"\.pyc$",
    r"venv",
    r"\.venv"
]

# Track processed skills for deduplication
processed_skills: Set[str] = set()
skill_sources: Dict[str, str] = {}  # skill_name -> source


def categorize_skill(skill_name: str, skill_path: Path) -> str:
    """Determine the category for a skill based on its name and content."""
    name_lower = skill_name.lower()

    # Check each category's keywords
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in name_lower:
                return category

    # Try to read SKILL.md for more context
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        try:
            content = skill_md.read_text().lower()
            for category, keywords in CATEGORY_KEYWORDS.items():
                for keyword in keywords:
                    if keyword in content[:500]:  # Check first 500 chars
                        return category
        except:
            pass

    # Default to development
    return "development"


def is_sensitive(path: Path) -> bool:
    """Check if a path contains sensitive data."""
    path_str = str(path)
    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, path_str):
            return True
    return False


def copy_skill(src: Path, dest_category: str, skill_name: str, source_label: str) -> bool:
    """Copy a skill to the appropriate category folder."""
    global processed_skills, skill_sources

    # Normalize skill name
    skill_name = skill_name.lower().replace(" ", "-").replace("_", "-")

    # Check for duplicates
    if skill_name in processed_skills:
        print(f"  [SKIP] Duplicate: {skill_name} (already from {skill_sources.get(skill_name, 'unknown')})")
        return False

    dest_dir = BASE_DIR / dest_category / skill_name

    try:
        if src.is_file():
            # Single file skill (like commands/*.md)
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest_dir / "SKILL.md")
        else:
            # Directory skill
            if dest_dir.exists():
                shutil.rmtree(dest_dir)

            # Copy with filtering
            def ignore_sensitive(directory, files):
                ignored = []
                for f in files:
                    full_path = Path(directory) / f
                    if is_sensitive(full_path):
                        ignored.append(f)
                return ignored

            shutil.copytree(src, dest_dir, ignore=ignore_sensitive)

        processed_skills.add(skill_name)
        skill_sources[skill_name] = source_label
        print(f"  [OK] {skill_name} -> {dest_category}/")
        return True

    except Exception as e:
        print(f"  [ERROR] {skill_name}: {e}")
        return False


def process_source(source_path: Path, source_label: str, is_skill_dir: bool = True):
    """Process all skills from a source directory."""
    print(f"\n{'='*60}")
    print(f"Processing: {source_label}")
    print(f"Path: {source_path}")
    print(f"{'='*60}")

    if not source_path.exists():
        print(f"  [WARN] Path does not exist: {source_path}")
        return

    count = 0

    if is_skill_dir:
        # Each subdirectory is a skill
        for item in sorted(source_path.iterdir()):
            if item.is_dir() and not item.name.startswith("."):
                # Check if it has SKILL.md or looks like a skill
                has_skill_md = (item / "SKILL.md").exists()
                has_readme = (item / "README.md").exists()

                if has_skill_md or has_readme or any(item.iterdir()):
                    category = categorize_skill(item.name, item)
                    if copy_skill(item, category, item.name, source_label):
                        count += 1
    else:
        # Source contains .md files directly (commands)
        for item in sorted(source_path.iterdir()):
            if item.is_file() and item.suffix == ".md":
                skill_name = item.stem
                category = categorize_skill(skill_name, item.parent)
                if copy_skill(item, category, skill_name, source_label):
                    count += 1

    print(f"\n  Total from {source_label}: {count}")


def main():
    print("="*60)
    print("CLAUDE SKILLS COLLECTION SCRIPT")
    print("="*60)

    # 1. Local skills
    process_source(LOCAL_SKILLS, "local-skills")

    # 2. Local commands
    process_source(LOCAL_COMMANDS, "local-commands", is_skill_dir=False)

    # 3. ailabs-393
    if Path("/tmp/ailabs-skills").exists():
        for subdir in ["packages/skills", "dist/skills"]:
            ailabs_path = Path("/tmp/ailabs-skills") / subdir
            if ailabs_path.exists():
                process_source(ailabs_path, "ailabs-393")
                break

    # 4. claude-ecosystem collections
    collections = [
        ("my-skills", ECOSYSTEM_DIR / "my-skills"),
        ("composio", ECOSYSTEM_DIR / "awesome-claude-skills-composio"),
        ("superpowers", ECOSYSTEM_DIR / "superpowers" / "skills"),
        ("scientific", ECOSYSTEM_DIR / "claude-scientific-skills" / "scientific-skills"),
        ("agents-wshobson", ECOSYSTEM_DIR / "agents-wshobson" / "plugins"),
        ("travisvn", ECOSYSTEM_DIR / "awesome-claude-skills-travisvn"),
    ]

    for name, path in collections:
        process_source(path, f"ecosystem-{name}")

    # 5. Nested skills in my-skills
    nested_dirs = [
        ECOSYSTEM_DIR / "my-skills" / "skills-repo",
        ECOSYSTEM_DIR / "my-skills" / "skills-anth",
        ECOSYSTEM_DIR / "my-skills" / "engineering-team",
        ECOSYSTEM_DIR / "my-skills" / "marketing-skill",
    ]

    for nested in nested_dirs:
        if nested.exists():
            # Process each subdirectory
            for subdir in nested.iterdir():
                if subdir.is_dir() and not subdir.name.startswith("."):
                    process_source(subdir, f"my-skills-{nested.name}")

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total unique skills collected: {len(processed_skills)}")
    print("\nBy category:")

    for category in sorted(BASE_DIR.iterdir()):
        if category.is_dir() and not category.name.startswith("."):
            skill_count = sum(1 for x in category.iterdir() if x.is_dir())
            if skill_count > 0:
                print(f"  {category.name}: {skill_count}")


if __name__ == "__main__":
    main()
