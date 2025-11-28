#!/usr/bin/env python3
"""
Convert Obsidian markdown files to GitHub-compatible markdown.
Converts [[#heading]] links to GitHub anchor format.
"""

import re
import os
from pathlib import Path


def heading_to_github_anchor(heading_text):
    """
    Convert heading text to GitHub anchor format.
    GitHub:
    - Converts to lowercase
    - Replaces spaces with hyphens
    - Removes special characters except hyphens
    - Removes emojis
    """
    # Remove emojis (basic emoji removal)
    anchor = re.sub(r'[^\w\s-]', '', heading_text)
    # Convert to lowercase and replace spaces with hyphens
    anchor = anchor.lower().strip().replace(' ', '-')
    # Remove multiple consecutive hyphens
    anchor = re.sub(r'-+', '-', anchor)
    # Remove leading/trailing hyphens
    anchor = anchor.strip('-')
    return anchor


def convert_obsidian_link(match):
    """Convert Obsidian [[#heading]] or [[#heading|text]] to GitHub format."""
    full_match = match.group(0)

    # Pattern: [[#heading|custom text]]
    if '|' in full_match:
        parts = full_match[3:-2].split('|')  # Remove [[ and ]]
        heading = parts[0]  # Remove the #
        link_text = parts[1]
        anchor = heading_to_github_anchor(heading)
        return f'[{link_text}](#{anchor})'

    # Pattern: [[#heading]]
    else:
        heading = full_match[3:-2]  # Remove [[# and ]]
        anchor = heading_to_github_anchor(heading)
        return f'[{heading}](#{anchor})'


def convert_file(file_path):
    """Convert a single markdown file from Obsidian to GitHub format."""
    print(f"Processing: {file_path}")

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create backup
    backup_path = f"{file_path}.backup"
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Convert [[#heading|text]] and [[#heading]] patterns
    # Pattern matches [[#...]] or [[#...|...]]
    pattern = r'\[\[#[^\]]+(?:\|[^\]]+)?\]\]'
    converted_content = re.sub(pattern, convert_obsidian_link, content)

    # Write the converted content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    print(f"✓ Converted: {file_path}")


def main():
    """Find and convert all markdown files in current directory and subdirectories."""
    print("Converting Obsidian markdown files to GitHub format...\n")

    # Find all .md files
    md_files = list(Path('.').rglob('*.md'))

    if not md_files:
        print("No markdown files found!")
        return

    for md_file in md_files:
        # Skip files in .git directory
        if '.git' in str(md_file):
            continue

        convert_file(md_file)

    print(f"\nConversion complete! Processed {len(md_files)} file(s).")
    print("Backup files created with .backup extension")
    print("\nTo remove backups after verification:")
    print("  find . -name '*.backup' -delete")
    print("\nTo restore from backup if needed:")
    print("  find . -name '*.backup' -exec sh -c 'mv \"$1\" \"${1%.backup}\"' _ {} \\;")


if __name__ == '__main__':
    main()
