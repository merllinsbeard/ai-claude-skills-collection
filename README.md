# AI Claude Skills Collection

A comprehensive collection of **300+ skills** for Claude Code, curated from multiple sources.

## What are Skills?

Skills are reusable prompts and instructions that extend Claude Code's capabilities. Each skill provides specialized knowledge, workflows, or domain expertise.

## Structure

Each skill is organized as a folder containing:
- `SKILL.md` - The skill definition and instructions
- `scripts/` - Optional helper scripts (if applicable)
- `references/` - Optional reference materials
- `{skill-name}.zip` - Packaged archive for easy installation

## Categories

### Development & Engineering
- `code-reviewer` - Code review automation
- `senior-architect` - System architecture guidance
- `senior-backend` / `senior-frontend` / `senior-fullstack`
- `senior-devops` / `senior-security` / `senior-secops`
- `test-driven-development` - TDD workflows
- `systematic-debugging` - Debugging methodology

### Document Processing
- `pdf` - PDF manipulation and extraction
- `docx` - Word document handling
- `xlsx` - Excel/spreadsheet operations
- `pptx` - PowerPoint generation

### Scientific & Research
- `pandas` / `polars` / `dask` - Data analysis
- `matplotlib` / `plotly` / `seaborn` - Visualization
- `scikit-learn` / `pytorch` / `transformers` - ML frameworks
- `biopython` / `rdkit` - Bioinformatics & chemistry
- 120+ more scientific tools

### Content & Marketing
- `content-research-writer` - Research-based content
- `seo-optimizer` - SEO optimization
- `social-media-generator` - Social media content

### Business & Strategy
- `product-manager-toolkit` - Product management
- `ceo-advisor` / `cto-advisor` - Executive advisory
- `startup-validator` - Startup validation

### Meta Skills
- `brainstorming` - Idea refinement
- `writing-plans` - Implementation planning
- `skill-creator` - Create new skills

## Installation

### Single Skill
```bash
# Copy skill folder to your Claude skills directory
cp -r skill-name ~/.claude/skills/
```

### Using ZIP Archive
```bash
# Extract and install
unzip skill-name/skill-name.zip -d ~/.claude/skills/
```

## Sources

This collection aggregates skills from:
- Local Claude Code skills
- [ailabs-393/ai-labs-claude-skills](https://github.com/ailabs-393/ai-labs-claude-skills)
- Claude Ecosystem community collections
- Scientific skills libraries
- Plugin marketplaces

## Contributing

To add a new skill:
1. Create a folder with your skill name
2. Add `SKILL.md` with frontmatter (name, description)
3. Include any helper scripts in `scripts/`
4. Create a zip archive
5. Submit a PR

## License

Individual skills may have their own licenses. Check each skill's folder for specific licensing information.

---

*Generated and curated for the Claude Code community*
