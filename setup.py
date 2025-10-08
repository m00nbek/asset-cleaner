#!/usr/bin/env python3
"""Setup script for Asset Cleaner."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="assetcleaner",
    version="1.0.0",
    author="nigga",
    description="Find and remove unused assets from Xcode projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/asset-cleaner",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "assetcleaner=assetcleaner.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="xcode assets ios macos cleanup unused",
)
