# Asset Cleaner - Quick Start

## 🎯 What You Have

A complete, production-ready Python package that can:
- Find unused assets in Xcode `.xcassets` catalogs
- Scan your entire codebase intelligently
- Generate detailed reports
- Safely delete unused assets
- Work from any directory via terminal command

## 📁 Location

```
~/Developer/asset-cleaner/
```

## ⚡ Quick Install & Test

### 1. Install Locally

```bash
cd ~/Developer/asset-cleaner
./install.sh
```

Or manually:

```bash
cd ~/Developer/asset-cleaner
pip3 install -e . --user
```

### 2. Test It

```bash
# Go to your Xcode project
cd ~/Developer/symptom-checker-ios

# Run the tool
assetcleaner
```

## 🌐 Publish to GitHub

### Step 1: Create GitHub Repo

1. Go to https://github.com/new
2. Repository name: `asset-cleaner`
3. Description: "Find and remove unused assets from Xcode projects"
4. Public repository
5. **Don't** check "Initialize with README" (we have one)
6. Click "Create repository"

### Step 2: Push Code

```bash
cd ~/Developer/asset-cleaner

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial release: Asset Cleaner v1.0.0"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/asset-cleaner.git

# Push
git branch -M main
git push -u origin main
```

### Step 3: Create Release

1. Go to your repo: `https://github.com/YOUR_USERNAME/asset-cleaner`
2. Click "Releases" → "Create a new release"
3. Click "Choose a tag" → type `v1.0.0` → "Create new tag"
4. Release title: `v1.0.0 - Initial Release`
5. Description:
```markdown
# Asset Cleaner v1.0.0

Find and remove unused assets from Xcode projects with intelligent name matching.

## Features
- 🔍 Smart asset detection
- 🎯 Multiple naming convention support
- 📊 Detailed usage reports
- 🗑️ Safe interactive deletion
- ⚡ Fast scanning

## Installation

### Via Homebrew
\`\`\`bash
brew tap YOUR_USERNAME/tap
brew install assetcleaner
\`\`\`

### Via pip
\`\`\`bash
pip3 install git+https://github.com/YOUR_USERNAME/asset-cleaner.git
\`\`\`

## Usage
\`\`\`bash
cd /path/to/xcode/project
assetcleaner
\`\`\`
```
6. Click "Publish release"

## 🍺 Setup Homebrew Tap

### Step 1: Create Tap Repository

1. Go to https://github.com/new
2. Repository name: `homebrew-tap`
3. Description: "Homebrew formulae"
4. Public
5. Click "Create repository"

### Step 2: Get Release SHA256

```bash
# Download your release tarball
curl -L https://github.com/YOUR_USERNAME/asset-cleaner/archive/v1.0.0.tar.gz -o asset-cleaner.tar.gz

# Get SHA256
shasum -a 256 asset-cleaner.tar.gz
# Copy the hash output
```

### Step 3: Update Formula

```bash
# Clone your tap
cd ~/Developer
git clone https://github.com/YOUR_USERNAME/homebrew-tap.git
cd homebrew-tap

# Copy formula
cp ~/Developer/asset-cleaner/assetcleaner.rb .

# Edit the formula
nano assetcleaner.rb
```

Update these lines:
```ruby
homepage "https://github.com/YOUR_USERNAME/asset-cleaner"
url "https://github.com/YOUR_USERNAME/asset-cleaner/archive/v1.0.0.tar.gz"
sha256 "PASTE_YOUR_SHA256_HERE"
```

### Step 4: Publish Tap

```bash
git add assetcleaner.rb
git commit -m "Add assetcleaner formula"
git push origin main
```

### Step 5: Test Installation

```bash
# Add your tap
brew tap YOUR_USERNAME/tap

# Install
brew install assetcleaner

# Test
assetcleaner --help
```

## 📦 Alternative: Direct Install from GitHub

Users can install directly without Homebrew:

```bash
pip3 install git+https://github.com/YOUR_USERNAME/asset-cleaner.git
```

## 🎉 Share with Others

Once published, share this installation command:

### For Homebrew Users:
```bash
brew tap YOUR_USERNAME/tap
brew install assetcleaner
```

### For pip Users:
```bash
pip3 install git+https://github.com/YOUR_USERNAME/asset-cleaner.git
```

### Usage:
```bash
cd /path/to/xcode/project
assetcleaner
```

## 📝 Update Your README

Before publishing, update `README.md`:

1. Replace `yourusername` with your actual GitHub username
2. Update the installation URLs
3. Add screenshots if desired
4. Add your contact info

## 🔄 Making Updates

When you make changes:

```bash
cd ~/Developer/asset-cleaner

# Make your changes
# ...

# Update version in assetcleaner/__init__.py and setup.py
# Then:

git add .
git commit -m "Version 1.1.0: Description of changes"
git tag v1.1.0
git push origin main --tags

# Create new release on GitHub
# Update Homebrew formula with new URL and SHA256
```

## ✅ Checklist

- [ ] Install locally and test
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Create v1.0.0 release
- [ ] Create homebrew-tap repository
- [ ] Update and publish formula
- [ ] Test installation via Homebrew
- [ ] Update README with your username
- [ ] Share with the community!

## 🆘 Need Help?

If you encounter issues:

1. Check Python version: `python3 --version` (needs 3.8+)
2. Check installation: `which assetcleaner`
3. Try reinstalling: `pip3 install --force-reinstall -e .`
4. Check PATH: `echo $PATH`

---

**You're all set!** 🚀

Your tool is ready to be shared with the world. Good luck!
