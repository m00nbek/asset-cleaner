#!/usr/bin/env python3
# Author: nigga

import os
import shutil
from pathlib import Path
from typing import List, Optional


ASSET_DIR_SUFFIXES = {
    ".imageset",
    ".appiconset",
    ".colorset",
    ".symbolset",
    ".dataset",
    ".stickerpack",
    ".stickersiconset",
    ".arresourcegroup",
}


def list_asset_dirs(assets_root: Path) -> List[Path]:
    found: List[Path] = []
    for root, dirnames, filenames in os.walk(assets_root):
        base = os.path.basename(root)
        for suffix in ASSET_DIR_SUFFIXES:
            if base.endswith(suffix):
                found.append(Path(root))
                break
    return found


def load_unused_list(result_file: Path) -> List[str]:
    if not result_file.exists():
        raise FileNotFoundError(f"Result file not found: {result_file}")
    names: List[str] = []
    for line in result_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            names.append(stripped)
    return names


def match_asset_dirs(asset_names: List[str], assets_root: Path) -> List[Path]:
    all_dirs = list_asset_dirs(assets_root)
    name_to_dirs = {}
    for d in all_dirs:
        base = d.name
        for suffix in ASSET_DIR_SUFFIXES:
            if base.endswith(suffix):
                logical_name = base[: -len(suffix)]
                name_to_dirs.setdefault(logical_name, []).append(d)
                break
    matched: List[Path] = []
    for name in asset_names:
        dirs = name_to_dirs.get(name, [])
        matched.extend(dirs)
    return matched


def delete_assets(assets_path: Path, unused_names: List[str], dry_run: bool = True) -> List[Path]:
    """
    Delete unused asset directories.
    Returns list of deleted paths.
    """
    dirs_to_delete = match_asset_dirs(unused_names, assets_path)
    deleted: List[Path] = []
    
    for d in sorted(dirs_to_delete, key=lambda p: str(p)):
        if not d.exists():
            continue
        if dry_run:
            print(f"DRY-RUN would delete: {d}")
        else:
            shutil.rmtree(d)
            print(f"Deleted: {d}")
            deleted.append(d)
    
    return deleted
