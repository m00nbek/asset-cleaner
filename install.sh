#!/bin/bash
# Quick installation script for Asset Cleaner

set -e

echo "🚀 Installing Asset Cleaner..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Install package
echo "📦 Installing assetcleaner package..."
pip3 install -e . --user

# Verify installation
if command -v assetcleaner &> /dev/null; then
    echo "✅ Installation successful!"
    echo ""
    echo "You can now use 'assetcleaner' from anywhere in your terminal."
    echo ""
    echo "Try it out:"
    echo "  cd /path/to/your/xcode/project"
    echo "  assetcleaner"
else
    echo "⚠️  Installation completed but 'assetcleaner' command not found in PATH."
    echo ""
    echo "You may need to add this to your PATH:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
    echo "Or run it with:"
    echo "  python3 -m assetcleaner"
fi
