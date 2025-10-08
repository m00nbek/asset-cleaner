# Asset Cleaner - Setup & Publishing Guide

## 📦 Project Structure

```
asset-cleaner/
├── assetcleaner/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point for python -m assetcleaner
│   ├── cli.py               # Main CLI interface
│   ├── scanner.py           # Asset scanning logic
│   └── deleter.py           # Asset deletion logic
├── setup.py                 # Package configuration
├── README.md                # Documentation
├── LICENSE                  # MIT License
├── MANIFEST.in              # Package manifest
├── .gitignore              # Git ignore rules
└── assetcleaner.rb         # Homebrew formula (template)
```

## 🚀 Local Installation & Testing

### 1. Install Locally (Development Mode)

```bash
cd ~/Developer/asset-cleaner
pip3 install -e .
```

This installs the package in "editable" mode, so changes to the code are immediately reflected.

### 2. Test the Command

```bash
# Navigate to any Xcode project
cd ~/Developer/your-xcode-project

# Run the tool
assetcleaner
```

### 3. Test with Python Module

```bash
python3 -m assetcleaner
```

## 📤 Publishing to GitHub

### 1. Initialize Git Repository

```bash
cd ~/Developer/asset-cleaner
git init
git add .
git commit -m "Initial commit: Asset Cleaner v1.0.0"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `asset-cleaner`
3. Don't initialize with README (we already have one)

### 3. Push to GitHub

```bash
git remote add origin https://github.com/m00nbek/asset-cleaner.git
git branch -M main
git push -u origin main
```

### 4. Create a Release

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `Asset Cleaner v1.0.0`
5. Description: Copy from README features section
6. Click "Publish release"

## 🍺 Publishing to Homebrew

### Option 1: Create Your Own Tap (Recommended for Personal Use)

#### 1. Create a Homebrew Tap Repository

```bash
# Create a new GitHub repo named "homebrew-tap"
# Then clone it locally
cd ~/Developer
git clone https://github.com/m00nbek/homebrew-tap.git
cd homebrew-tap
```

#### 2. Update the Formula

First, get the SHA256 of your release:

```bash
# After creating a GitHub release, download the tarball
curl -L https://github.com/m00nbek/asset-cleaner/archive/v1.0.0.tar.gz -o asset-cleaner.tar.gz

# Calculate SHA256
shasum -a 256 asset-cleaner.tar.gz
```

#### 3. Copy and Update Formula

```bash
# Copy the formula to your tap
cp ~/Developer/asset-cleaner/assetcleaner.rb ~/Developer/homebrew-tap/assetcleaner.rb

# The formula is already updated with correct URLs and SHA256!
```

#### 4. Publish Your Tap

```bash
cd ~/Developer/homebrew-tap
git add assetcleaner.rb
git commit -m "Add assetcleaner formula"
git push origin main
```

#### 5. Install from Your Tap

```bash
brew tap m00nbek/tap
brew install assetcleaner
```

### Option 2: Submit to Homebrew Core (For Public Distribution)

This requires more work and review:

1. Fork https://github.com/Homebrew/homebrew-core
2. Add your formula to `Formula/assetcleaner.rb`
3. Test thoroughly
4. Submit a Pull Request
5. Wait for review and approval

## 📦 Publishing to PyPI (Optional)

To make it installable via `pip install assetcleaner`:

### 1. Create PyPI Account

Go to https://pypi.org/account/register/

### 2. Build Distribution

```bash
cd ~/Developer/asset-cleaner
pip3 install build twine
python3 -m build
```

### 3. Upload to PyPI

```bash
python3 -m twine upload dist/*
```

### 4. Install from PyPI

```bash
pip3 install assetcleaner
```

## 🔧 Making it Globally Available (Without Homebrew)

### Option 1: Add to PATH

Add this to your `~/.zshrc` or `~/.bash_profile`:

```bash
export PATH="$HOME/Developer/asset-cleaner:$PATH"
```

Then create a wrapper script:

```bash
cat > ~/Developer/asset-cleaner/assetcleaner << 'EOF'
#!/usr/bin/env python3
from assetcleaner.cli import main
import sys
sys.exit(main())
EOF

chmod +x ~/Developer/asset-cleaner/assetcleaner
```

### Option 2: Create Symlink

```bash
# After pip install -e .
ln -s $(which assetcleaner) /usr/local/bin/assetcleaner
```

## ✅ Verification

Test that everything works:

```bash
# Should show help/run the tool
assetcleaner

# Should show version
python3 -c "import assetcleaner; print(assetcleaner.__version__)"
```

## 📝 Updating the Package

### 1. Make Changes

Edit files in `~/Developer/asset-cleaner/assetcleaner/`

### 2. Update Version

Update version in:
- `assetcleaner/__init__.py`
- `setup.py`

### 3. Commit and Release

```bash
git add .
git commit -m "Version 1.1.0: Add new features"
git tag v1.1.0
git push origin main --tags
```

### 4. Update Homebrew Formula

Update the `url` and `sha256` in your tap's formula, then:

```bash
cd ~/Developer/homebrew-tap
git add assetcleaner.rb
git commit -m "Update assetcleaner to 1.1.0"
git push
```

### 5. Users Update

```bash
brew update
brew upgrade assetcleaner
```

## 🎯 Quick Start for Users

Once published, users can install with:

```bash
# Via Homebrew (your tap)
brew tap m00nbek/tap
brew install assetcleaner

# Via pip
pip3 install assetcleaner

# Then use it
cd /path/to/xcode/project
assetcleaner
```

## 🐛 Troubleshooting

### Command not found

```bash
# Check if installed
which assetcleaner

# Reinstall
pip3 install --force-reinstall assetcleaner
```

### Python version issues

Ensure Python 3.8+ is installed:

```bash
python3 --version
```

### Permission errors

Use `--user` flag:

```bash
pip3 install --user assetcleaner
```

---

## 📚 Next Steps

1. ✅ Test locally with `pip install -e .`
2. ✅ Push to GitHub
3. ✅ Create a release
4. ✅ Set up Homebrew tap
5. ✅ Share with the community!

Happy coding! 🚀
