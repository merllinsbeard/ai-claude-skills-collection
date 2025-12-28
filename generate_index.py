#!/usr/bin/env python3
"""Generate SKILLS_INDEX.md with all skills organized by category."""

import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/Users/merlin/Dev/ai-claude-skills-collection")

CATEGORY_DESCRIPTIONS = {
    "development": "Code, architecture, review, testing, debugging",
    "scientific": "Data science, bioinformatics, chemistry, research tools",
    "documents": "PDF, Word, Excel, PowerPoint, document processing",
    "content": "SEO, copywriting, social media, marketing content",
    "business": "Product management, strategy, compliance, advisory",
    "devops": "Docker, Kubernetes, CI/CD, cloud infrastructure",
    "ai-ml": "LLM, prompts, agents, machine learning",
    "automation": "n8n, MCP, browser automation, workflows",
    "meta": "Planning, brainstorming, skill creation, frameworks"
}

def get_skill_description(skill_path: Path) -> str:
    """Extract description from SKILL.md if available."""
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        try:
            content = skill_md.read_text()
            for line in content.split('\n'):
                if line.startswith('description:'):
                    return line.replace('description:', '').strip().strip('"\'')
        except:
            pass
    return ""


def main():
    lines = [
        "# Skills Index",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "## Summary",
        "",
        "| Category | Count | Description |",
        "|----------|-------|-------------|"
    ]

    # Count skills per category
    category_counts = {}
    all_skills = {}

    for category in sorted(BASE_DIR.iterdir()):
        if category.is_dir() and not category.name.startswith('.') and category.name in CATEGORY_DESCRIPTIONS:
            skills = [s for s in category.iterdir() if s.is_dir()]
            category_counts[category.name] = len(skills)
            all_skills[category.name] = sorted(skills, key=lambda x: x.name)

    total = sum(category_counts.values())

    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        desc = CATEGORY_DESCRIPTIONS.get(cat, "")
        lines.append(f"| [{cat}](#{cat}) | {count} | {desc} |")

    lines.append(f"| **Total** | **{total}** | |")
    lines.append("")

    # Generate detailed sections
    for category, skills in sorted(all_skills.items(), key=lambda x: -len(x[1])):
        lines.append(f"## {category.capitalize()}")
        lines.append("")
        lines.append(f"*{CATEGORY_DESCRIPTIONS.get(category, '')}*")
        lines.append("")
        lines.append("| Skill | Description |")
        lines.append("|-------|-------------|")

        for skill in skills:
            desc = get_skill_description(skill)
            desc_short = desc[:80] + "..." if len(desc) > 80 else desc
            lines.append(f"| [{skill.name}]({category}/{skill.name}) | {desc_short} |")

        lines.append("")

    # Write file
    index_path = BASE_DIR / "SKILLS_INDEX.md"
    index_path.write_text('\n'.join(lines))
    print(f"Generated {index_path}")
    print(f"Total skills indexed: {total}")


if __name__ == "__main__":
    main()
