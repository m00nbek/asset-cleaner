#!/usr/bin/env python3
# Author: nigga

import os
import sys
from pathlib import Path
from typing import List, Optional

from .scanner import find_assets_directory, scan_assets, EXCLUDE_DIR_NAMES
from .deleter import delete_assets, load_unused_list, format_size


def print_header():
    print("\n" + "=" * 60)
    print("  Asset Cleaner by nigga")
    print("=" * 60)
    print("Find and remove unused assets from your Xcode projects.\n")


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    while True:
        ans = input(f"{prompt} {suffix} ").strip().lower()
        if not ans:
            return default
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please answer y or n.")


def find_all_xcassets(root: Path) -> List[Path]:
    """Find all .xcassets directories in the project."""
    found: List[Path] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
        for d in dirnames:
            if d.endswith(".xcassets"):
                found.append(Path(current_root) / d)
    return sorted(found, key=lambda p: str(p))


def choose_xcassets(project_root: Path) -> Optional[Path]:
    """List available .xcassets and let user choose."""
    print("Searching for .xcassets directories...\n")
    candidates = find_all_xcassets(project_root)
    
    if not candidates:
        print("❌ No .xcassets directories found in the project.")
        return None
    
    if len(candidates) == 1:
        rel_path = candidates[0].relative_to(project_root) if candidates[0].is_relative_to(project_root) else candidates[0]
        print(f"Found 1 asset catalog: {rel_path}")
        if ask_yes_no("Use this catalog?", default=True):
            return candidates[0]
        return None
    
    print(f"Found {len(candidates)} asset catalogs:\n")
    for idx, path in enumerate(candidates, start=1):
        rel_path = path.relative_to(project_root) if path.is_relative_to(project_root) else path
        print(f"  {idx}. {rel_path}")
    
    while True:
        choice = input(f"\nSelect a catalog (1-{len(candidates)}) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            return None
        try:
            idx = int(choice)
            if 1 <= idx <= len(candidates):
                return candidates[idx - 1]
            print(f"Please enter a number between 1 and {len(candidates)}.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")


def main() -> int:
    """Main entry point for the CLI."""
    print_header()
    
    # Determine project root (current working directory)
    project_root = Path.cwd()
    output_dir = project_root / ".assetcleaner"
    output_dir.mkdir(exist_ok=True)
    
    # Let user choose asset catalog
    assets_path = choose_xcassets(project_root)
    if not assets_path:
        print("\n❌ No asset catalog selected. Exiting.")
        return 1
    
    # Run scan
    print(f"\n🔍 Scanning for asset usage in: {assets_path.name}")
    try:
        assets_list, unused_report, used_report = scan_assets(
            assets_path=assets_path,
            project_root=project_root,
            output_dir=output_dir
        )
    except Exception as e:
        print(f"\n❌ Scan failed: {e}")
        return 1
    
    print("\n✅ Scan complete!")
    print(f"   📄 All assets with variants: {assets_list}")
    print(f"   📄 Used assets report:       {used_report}")
    print(f"   📄 Unused assets report:     {unused_report}")
    
    # Read unused list
    try:
        unused_names = load_unused_list(unused_report)
    except Exception as e:
        print(f"\n❌ Error reading results: {e}")
        return 1
    
    if not unused_names:
        print("\n✅ No unused assets detected. Your project is clean!")
        # Cleanup temporary directory
        if output_dir.exists():
            import shutil
            shutil.rmtree(output_dir)
        return 0
    
    print(f"\n📋 Found {len(unused_names)} unused asset(s):")
    for name in unused_names[:10]:  # Show first 10
        print(f"   • {name}")
    if len(unused_names) > 10:
        print(f"   ... and {len(unused_names) - 10} more")
    
    if not ask_yes_no("\nWould you like to review and optionally delete unused assets?", default=True):
        print("\n👋 Done. Reports saved to .assetcleaner/")
        return 0
    
    if not ask_yes_no("\n🗑️  Delete these unused assets from .xcassets?", default=False):
        print("\nSkipping deletion. Reports saved to .assetcleaner/")
        return 0
    
    # Delete unused assets
    print("\n🗑️  Deleting unused assets...")
    try:
        deleted, total_bytes = delete_assets(assets_path, unused_names, dry_run=False)
        print(f"\n✅ Successfully deleted {len(deleted)} asset(s).")
        print(f"💾 Storage freed: {format_size(total_bytes)}")
    except Exception as e:
        print(f"\n❌ Deletion failed: {e}")
        return 1
    
    # Cleanup temporary directory
    print("\n🧹 Cleaning up temporary files...")
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
        print(f"   Removed {output_dir}")
    
    print("\n✨ All done! Your asset catalog is now clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
