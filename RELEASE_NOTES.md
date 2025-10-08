# Release Notes

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
