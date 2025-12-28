#!/usr/bin/env python3
"""
Notion Export Processor
Converts Notion exports (CSV and MD files) into a unified markdown document.
"""

import csv
import os
import sys
import glob
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

def find_files(directory: str = '.') -> Tuple[List[str], List[str], List[str]]:
    """Find all CSV, MD, and image files in the directory."""
    # Find CSV files
    csv_files = glob.glob(os.path.join(directory, "*.csv"))

    # Find markdown files
    md_files = glob.glob(os.path.join(directory, "*.md"))

    # Find image files
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.webp']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, ext)))

    return csv_files, md_files, image_files

def find_files_for_cleanup(directory: str = '.', exclude_file: str = None) -> Tuple[List[str], List[str]]:
    """Find CSV and MD files for deletion, excluding the output file."""
    # Find CSV files
    csv_files = glob.glob(os.path.join(directory, "*.csv"))

    # Find markdown files, excluding the output file
    md_files = glob.glob(os.path.join(directory, "*.md"))
    if exclude_file:
        md_files = [f for f in md_files if f != exclude_file]

    return csv_files, md_files

def csv_to_markdown_table(csv_file: str) -> str:
    """Convert a CSV file to a markdown table."""
    output = []

    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            rows = list(reader)

        if not rows:
            return ""

        # Extract table name from filename (remove Notion ID)
        table_name = os.path.basename(csv_file)
        if ' ' in table_name:
            table_name = ' '.join(table_name.split(' ')[:-1])  # Remove last part (usually the ID)
        table_name = table_name.replace('.csv', '').strip()

        output.append(f"## Table: {table_name}\n")

        # Convert to markdown table
        headers = rows[0]
        output.append('| ' + ' | '.join(headers) + ' |')
        output.append('|' + '---|' * len(headers))

        for row in rows[1:]:
            # Clean up cells (remove newlines, handle empty cells)
            cleaned_row = [cell.replace('\n', ' ').replace('|', '\\|') if cell else '' for cell in row]
            output.append('| ' + ' | '.join(cleaned_row) + ' |')

        output.append('')

    except Exception as e:
        print(f"Error processing {csv_file}: {e}")
        return f"## Error reading {csv_file}\n\n{e}\n"

    return '\n'.join(output)

def process_markdown_file(md_file: str, image_files: List[str]) -> str:
    """Process a markdown file and add image references."""
    output = []

    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract page title from filename (remove Notion ID)
        page_name = os.path.basename(md_file)
        if ' ' in page_name:
            parts = page_name.split(' ')
            if len(parts) > 1 and len(parts[-1].split('.')[0]) > 10:  # Likely an ID
                page_name = ' '.join(parts[:-1])
        page_name = page_name.replace('.md', '').strip()

        output.append(f"## Page: {page_name}\n")

        # Add the content
        output.append(content)
        output.append('')

        # Check if there are images that match this page name
        base_name = os.path.basename(md_file).replace('.md', '')
        for img in image_files:
            img_basename = os.path.basename(img)
            if base_name in img_basename:
                img_name = os.path.splitext(img_basename)[0]
                img_ext = os.path.splitext(img_basename)[1]
                # Clean image name (remove Notion ID)
                if ' ' in img_name:
                    parts = img_name.split(' ')
                    if len(parts) > 1 and len(parts[-1]) > 10:
                        img_name = ' '.join(parts[:-1])
                output.append(f"![{img_name}]({img_basename})")

        output.append('')
        output.append('---')
        output.append('')

    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return f"## Error reading {md_file}\n\n{e}\n"

    return '\n'.join(output)

def generate_table_of_contents(csv_files: List[str], md_files: List[str]) -> str:
    """Generate a table of contents."""
    output = ["## Table of Contents\n"]

    output.append("### Tables\n")
    for i, csv_file in enumerate(csv_files, 1):
        name = os.path.basename(csv_file).replace('.csv', '')
        output.append(f"- [Table {i}: {name}](#table-{i}-{name.lower().replace(' ', '-')})")

    output.append("")
    output.append("### Pages\n")
    for i, md_file in enumerate(md_files, 1):
        name = os.path.basename(md_file).replace('.md', '')
        output.append(f"- [Page {i}: {name}](#page-{i}-{name.lower().replace(' ', '-')})")

    output.append("")
    return '\n'.join(output)

def generate_output_name(csv_files: List[str], md_files: List[str]) -> str:
    """Generate meaningful output name from the first file."""
    # Try to get name from first CSV file
    if csv_files:
        filename = os.path.basename(csv_files[0])
        # Remove Notion ID (last part after space if it looks like an ID)
        parts = filename.split(' ')
        if len(parts) > 1 and len(parts[-1].split('.')[0]) > 10:
            name_parts = parts[:-1]
        else:
            name_parts = parts
        base_name = ' '.join(name_parts).replace('.csv', '')
    # If no CSV, try from first MD file
    elif md_files:
        filename = os.path.basename(md_files[0])
        # Remove Notion ID
        parts = filename.split(' ')
        if len(parts) > 1 and len(parts[-1].split('.')[0]) > 10:
            name_parts = parts[:-1]
        else:
            name_parts = parts
        base_name = ' '.join(name_parts).replace('.md', '')
    else:
        base_name = "notion-export"

    # Clean up the name (remove special characters)
    base_name = base_name.replace('/', '-').replace('\\', '-')

    # Add date
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = f"{base_name}-{date_str}.md"

    return output_file

def main():
    """Main function to process all files."""
    directory = '.'

    print("Scanning for Notion export files...")
    csv_files, md_files, image_files = find_files(directory)

    print(f"Found {len(csv_files)} CSV file(s)")
    print(f"Found {len(md_files)} Markdown file(s)")
    print(f"Found {len(image_files)} Image file(s)")

    if not csv_files and not md_files:
        print("No CSV or Markdown files found. Exiting.")
        sys.exit(0)

    # Generate meaningful output filename
    output_file = generate_output_name(csv_files, md_files)

    # Store the created filename in global variable for exclusion
    global created_output_filename
    created_output_filename = output_file

    print(f"\nGenerating unified export: {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f"# Notion Export - Unified Document\n")
        f.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

        # Write table of contents
        f.write(generate_table_of_contents(csv_files, md_files))
        f.write("\n")

        # Process CSV files
        if csv_files:
            f.write("---\n\n")
            f.write("## Tables\n\n")
            for i, csv_file in enumerate(csv_files, 1):
                print(f"Processing CSV: {os.path.basename(csv_file)}")
                table_content = csv_to_markdown_table(csv_file)
                f.write(table_content)
                f.write("\n")

        # Process Markdown files
        if md_files:
            f.write("---\n\n")
            f.write("## Pages\n\n")
            for i, md_file in enumerate(md_files, 1):
                print(f"Processing Markdown: {os.path.basename(md_file)}")
                md_content = process_markdown_file(md_file, image_files)
                f.write(md_content)
                f.write("\n")

    print(f"\n✅ Unified export created: {output_file}")
    print(f"\nThe following files were processed:")
    for csv in csv_files:
        print(f"  - {os.path.basename(csv)}")
    for md in md_files:
        print(f"  - {os.path.basename(md)}")
    for img in image_files:
        print(f"  - {os.path.basename(img)} (referenced)")

    # Delete original files (CSV and MD, keep images)
    print(f"\n🗑️  Cleaning up original files...")
    deleted_count = 0

    # Get list of files for deletion, excluding the output file
    csv_cleanup_files, md_cleanup_files = find_files_for_cleanup(directory, output_file)

    total_files_to_delete = len(csv_cleanup_files) + len(md_cleanup_files)
    print(f"Found {total_files_to_delete} files to delete (excluding {output_file})")

    for csv in csv_cleanup_files:
        try:
            os.remove(csv)
            print(f"  Deleted: {os.path.basename(csv)}")
            deleted_count += 1
        except Exception as e:
            print(f"  Failed to delete {csv}: {e}")

    for md in md_cleanup_files:
        try:
            os.remove(md)
            print(f"  Deleted: {os.path.basename(md)}")
            deleted_count += 1
        except Exception as e:
            print(f"  Failed to delete {md}: {e}")

    print(f"\n✅ {deleted_count} files deleted. Only {output_file} remains with text content.")
    print(f"\nImage files were not deleted and remain in the directory.")

# Global variable to store created output filename for exclusion
created_output_filename = None

def find_files_for_cleanup(directory: str = '.', exclude_file: str = None) -> Tuple[List[str], List[str]]:
    """Find CSV and MD files for deletion, excluding the output file."""
    # Find CSV files
    csv_files = glob.glob(os.path.join(directory, "*.csv"))

    # Find markdown files, excluding the output file
    md_files = glob.glob(os.path.join(directory, "*.md"))
    if exclude_file:
        md_files = [f for f in md_files if f != exclude_file]
    # Also exclude any file that starts with our created pattern
    if created_output_filename:
        md_files = [f for f in md_files if not f.endswith(created_output_filename)]

    return csv_files, md_files

if __name__ == "__main__":
    main()
