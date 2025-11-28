# Kotlin Cheatsheet

A comprehensive collection of Kotlin programming notes and cheatsheets.

## Contents

- [Kotlin Fundamental](./Kotlin/Kotlin%20Fundamental.md) - Core language concepts, syntax, and basics
- [Kotlin OOP](./Kotlin/Kotlin%20OOP.md) - Object-oriented programming in Kotlin
- [Kotlin Collection](./Kotlin/Kotlin%20Collection.md) - Working with collections, lists, sets, and maps
- [Kotlin Generic](./Kotlin/Kotlin%20Generic.md) - Generic types and functions
- [Kotlin Coroutine](./Kotlin/Kotlin%20Coroutine.md) - Asynchronous programming with coroutines

## Credits

Based on materials by **Eko Kurniawan Khannedy** (Programmer Zaman Now)

- Website: [programmerzamannow.com](https://www.programmerzamannow.com/)
- YouTube: [Programmer Zaman Now](https://youtube.com/c/ProgrammerZamanNow)

## Format Compatibility

These markdown files have been formatted to work correctly on GitHub while maintaining compatibility with Obsidian.

### Converting Obsidian Links to GitHub Format

If you've made changes in Obsidian and need to convert the links back to GitHub format:

```bash
# Run the conversion script
python3 convert_obsidian_to_github.py
```

This will:
- Convert `[heading](#heading)` links to `[heading](#anchor)` format
- Create `.backup` files for safety
- Preserve all other markdown formatting

### Removing Backup Files

After verifying the conversion worked correctly:

```bash
find . -name '*.backup' -delete
```

### Restoring from Backup

If something went wrong:

```bash
find . -name '*.backup' -exec sh -c 'mv "$1" "${1%.backup}"' _ {} \;
```

## License

Educational content - please refer to original author's licensing terms.
