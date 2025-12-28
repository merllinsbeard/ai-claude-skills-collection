# Notion Export - Export to Markdown
This skill processes Notion database and page exports, converting them into a unified markdown document structure.

## Usage
```
skill: "notion-export"
```

## What it does
1. **Loads all CSV files** from Notion database exports and converts them to markdown tables
2. **Reads all Markdown files** from exported pages and database entries
3. **Extracts content** from markdown files, excluding binary data
4. **Handles image references** and creates markdown links
5. **Creates a single unified file** with all content properly structured
6. **Preserves hierarchy** and relationships between data

## Process
```
1. Read directory structure
2. Find all CSV files (Notion database exports)
3. Find all markdown files
4. For each CSV: Convert to markdown table format with header
5. For each markdown: Extract text content
6. Detect image files and create references
7. Create index with table of contents
8. Produce unified markdown file
```

## Output format
```markdown
# Notion Export - [Database Name]

## Table of Contents
- [Table 1: [CSV1 Name]](#table-1)
- [Page 1: [MD1 Name]](#page-1)
- [Page 2: [MD2 Name]](#page-2)
...

## Table 1: [CSV Name]

| Column1 | Column2 | Column3 |
|---------|---------|---------|
| Value1 | Value2 | Value3 |
...

## Page 1: [Page Title]

[Page content here...]
[Image references as: ![Image Description](image_filename.png)]

---
```

## Special handling
- **CSV files**: Parsed and converted to markdown tables
- **Binary files**: Excluded from content (images are referenced but not embedded)
- **Relative paths**: Image links use relative paths
- **Metadata**: File names and paths preserved as context
- **Large files**: Handles large datasets efficiently

## Example transformation
**Input files:**
- `My Database 12345.csv`
- `Page Title abc123.md`
- `Image 1.png`

**Output:**
```markdown
# Notion Export - My Database

## Table of Contents
- [Table 1: My Database](#table-1)
- [Page 1: Page Title](#page-1)

## Table 1: My Database
| Name | Description | Status |
|------|-------------|--------|
| Item 1 | Description 1 | Active |
| Item 2 | Description 2 | Done |

## Page 1: Page Title

This is the page content...

![Image 1](Image 1.png)

---
```

## Requirements
- Directory with Notion export files
- CSV files use standard comma separation (UTF-8 BOM optional)
- Markdown files have `.md` extension
- Image files have standard extensions (png, jpg, jpeg, gif, svg)

## Files processed
- `*.csv` - Notion database exports
- `*.md` - Notion page exports
- `*.png`, `*.jpg`, `*.jpeg`, `*.gif`, `*.svg` - Images (referenced, not embedded)
