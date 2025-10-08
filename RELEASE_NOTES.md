# Release Notes

## v1.1.0 (2025-10-08)

### What's New
- 💾 **Storage Reporting**: Shows the size of each deleted asset and total storage freed
- 🧹 **Automatic Cleanup**: Removes `.assetcleaner` temporary directory after completion
- ✨ **Better UX**: More informative output with storage metrics

### Features
- Display individual asset sizes during deletion (e.g., "Deleted: old_icon.imageset (125.3 KB)")
- Show total storage freed at the end (e.g., "Storage freed: 2.5 MB")
- Automatically clean up temporary `.assetcleaner` folder after process completes
- Clean up temp folder even when no unused assets are found

### Installation

```bash
# Via Homebrew
brew tap m00nbek/tap
brew upgrade assetcleaner  # If already installed
brew install assetcleaner  # Fresh install
```

### Technical Details
- **Version**: 1.1.0
- **SHA256**: `089bdffa74df43be1f25660f84507e4b0393703b1f891949ea148ef9e6bc305e`
- **Release URL**: https://github.com/m00nbek/asset-cleaner/archive/refs/tags/v1.1.0.tar.gz

---

## v1.0.1 (2025-10-08)

### What's Changed
- 🔧 Updated all documentation with correct GitHub username (`m00nbek`)
- 📝 Removed confidential project references (replaced with generic examples)
- 🔗 Fixed all GitHub URLs in installation instructions
- ✨ Added comprehensive release and publishing guides
- 📦 Updated Homebrew formula with correct SHA256 hash

### Installation

```bash
# Via Homebrew
brew tap m00nbek/tap
brew install assetcleaner

# Upgrade from v1.0.0
brew upgrade assetcleaner
```

### Files Updated
- README.md
- QUICKSTART.md  
- SETUP_GUIDE.md
- setup.py
- Homebrew formula

### Technical Details
- **Version**: 1.0.1
- **SHA256**: `705d4fbef5f139f6281764bece4a72eb22de06d4fbc3227aa78b93c5636cfc0d`
- **Release URL**: https://github.com/m00nbek/asset-cleaner/archive/refs/tags/v1.0.1.tar.gz

---

## v1.0.0 (2025-10-08)

### Initial Release

🎉 First public release of Asset Cleaner!

### Features
- 🔍 Smart asset detection with automatic `.xcassets` directory discovery
- 🎯 Intelligent naming convention matching (camelCase, snake_case, PascalCase, etc.)
- 📊 Detailed reports of used and unused assets
- 🗑️ Safe interactive deletion with confirmation prompts
- ⚡ Fast scanning of large codebases
- 📁 Support for multiple asset types (imagesets, colorsets, etc.)

### Installation

```bash
brew tap m00nbek/tap
brew install assetcleaner
```

### Usage

```bash
cd /path/to/your/xcode/project
assetcleaner
```

### Technical Details
- **Version**: 1.0.0
- **SHA256**: `dbd705a41f87706c4d5a572cc10c3bf36696f9980753887604aa0d862a13fb23`
- **Release URL**: https://github.com/m00nbek/asset-cleaner/archive/refs/tags/v1.0.0.tar.gz
