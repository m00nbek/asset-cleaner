# Asset Cleaner

> Find and remove unused assets from your Xcode projects

Asset Cleaner is a powerful command-line tool that scans your Xcode projects to identify unused assets in `.xcassets` catalogs. It intelligently detects various naming conventions (camelCase, snake_case, PascalCase, etc.) and helps you clean up your project by removing assets that are no longer referenced in your code.

## Features

- 🔍 **Smart Detection**: Automatically finds all `.xcassets` directories in your project
- 🎯 **Intelligent Matching**: Detects assets referenced in multiple naming conventions:
  - `delete_icon` → `deleteIcon`, `DeleteIcon`, `delete-icon`, etc.
  - `aboutSC_en` → `aboutSCEn` (special underscore handling)
- 📊 **Detailed Reports**: Generates comprehensive reports of used and unused assets
- 🗑️ **Safe Deletion**: Interactive prompts before deleting anything
- 🚀 **Fast Scanning**: Efficiently scans large codebases
- 📁 **Multiple Formats**: Supports various Xcode asset types:
  - Image sets (`.imageset`)
  - App icons (`.appiconset`)
  - Color sets (`.colorset`)
  - Symbol sets (`.symbolset`)
  - Data sets (`.dataset`)
  - And more...

## Installation

### Via Homebrew (Recommended)

```bash
brew tap yourusername/tap
brew install assetcleaner
```

### Via pip

```bash
pip install assetcleaner
```

### From Source

```bash
git clone https://github.com/yourusername/asset-cleaner.git
cd asset-cleaner
pip install -e .
```

## Usage

Navigate to your Xcode project directory and run:

```bash
assetcleaner
```

The tool will:
1. Search for all `.xcassets` directories
2. Let you choose which catalog to scan
3. Scan your project for asset usage
4. Generate reports in `.assetcleaner/` directory
5. Optionally delete unused assets

### Example Output

```
============================================================
  Asset Cleaner by nigga
============================================================
Find and remove unused assets from your Xcode projects.

Searching for .xcassets directories...

Found 1 asset catalog: Symptom Checker/Symptom Checker/Resources/Assets.xcassets
Use this catalog? [Y/n] y

🔍 Scanning for asset usage in: Assets.xcassets

✅ Scan complete!
   📄 All assets with variants: .assetcleaner/assets_list.txt
   📄 Used assets report:       .assetcleaner/used_result.txt
   📄 Unused assets report:     .assetcleaner/result.txt

📋 Found 15 unused asset(s):
   • old_logo
   • deprecated_icon
   • test_image
   ... and 12 more

Would you like to review and optionally delete unused assets? [Y/n] y

🗑️  Delete these unused assets from .xcassets? [y/N] y

🗑️  Deleting unused assets...
Deleted: /path/to/Assets.xcassets/old_logo.imageset
Deleted: /path/to/Assets.xcassets/deprecated_icon.imageset
...

✅ Successfully deleted 15 asset(s).

✨ All done! Your asset catalog is now clean.
```

## How It Works

1. **Asset Discovery**: Scans `.xcassets` directories for all asset types
2. **Variant Generation**: Creates multiple naming variants for each asset:
   - Original name
   - camelCase
   - snake_case
   - PascalCase
   - kebab-case
   - Special transformations (e.g., `name_en` → `nameEn`)
3. **Code Scanning**: Searches through your codebase (`.swift`, `.m`, `.h`, `.storyboard`, `.xib`, etc.)
4. **Usage Detection**: Matches any variant of the asset name in your code
5. **Report Generation**: Creates detailed reports of used and unused assets
6. **Safe Cleanup**: Optionally removes unused assets with confirmation

## File Extensions Scanned

By default, Asset Cleaner scans these file types:
- `.swift` - Swift source files
- `.m`, `.mm`, `.h` - Objective-C/C++ files
- `.storyboard`, `.xib` - Interface Builder files
- `.plist` - Property list files
- `.json` - JSON configuration files
- `.md` - Markdown documentation
- `.xcstrings` - String catalogs

## Excluded Directories

The following directories are automatically excluded from scanning:
- `.git`
- `Pods`
- `DerivedData`
- `build`
- `.build`

## Output Files

All reports are saved to `.assetcleaner/` in your project root:

- **`assets_list.txt`**: Complete list of all assets with their naming variants
- **`result.txt`**: List of unused assets (not found in code)
- **`used_result.txt`**: Detailed report of used assets with file locations and line numbers

## Requirements

- Python 3.8 or higher
- Xcode project with `.xcassets` catalogs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Author

Created by nigga

## Support

If you encounter any issues or have questions, please file an issue on GitHub.

---

**Note**: Always backup your project before running asset cleanup operations. While Asset Cleaner is designed to be safe, it's always better to be cautious with automated deletions.
