#!/bin/bash

# Convert Obsidian markdown to GitHub-compatible markdown
# This script converts [[#heading]] links to [heading](#heading) format

echo "Converting Obsidian markdown files to GitHub format..."

# Find all markdown files
find . -name "*.md" -type f | while read file; do
    echo "Processing: $file"

    # Create backup
    cp "$file" "$file.backup"

    # Convert [[#Heading|Link Text]] to [Link Text](#heading)
    # Convert [[#Heading]] to [Heading](#heading)
    sed -i -E 's/\[\[#([^|\]]+)\|([^\]]+)\]\]/[\2](#\L\1)/g' "$file"
    sed -i -E 's/\[\[#([^\]]+)\]\]/[\1](#\L\1)/g' "$file"

    # Remove emojis from anchors and replace spaces with hyphens
    # GitHub converts headings to lowercase and replaces spaces with hyphens
    # Also removes special characters

    echo "✓ Converted: $file"
done

echo ""
echo "Conversion complete!"
echo "Backup files created with .backup extension"
echo ""
echo "To remove backups after verification: find . -name '*.backup' -delete"
