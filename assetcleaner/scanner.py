#!/usr/bin/env python3
# Author: nigga

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple, Optional


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


DEFAULT_SCAN_FILE_EXTENSIONS = {
    ".swift",
    ".m",
    ".mm",
    ".h",
    ".storyboard",
    ".xib",
    ".plist",
    ".json",
    ".md",
    ".xcstrings",
}


EXCLUDE_DIR_NAMES = {
    ".git",
    "DerivedData",
    "build",
    "Pods",
    ".build",
}


def split_identifier_parts(text: str) -> List[str]:
    """Split string into constituent parts (handles snake, kebab, camel, Pascal)."""
    if not text:
        return []

    # Replace separators with space
    normalized = re.sub(r"[-_]+", " ", text)

    parts: List[str] = []
    for chunk in normalized.split():
        # Split camel/PascalCase boundaries: FooBar -> Foo Bar, deleteIcon -> delete Icon
        split = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", chunk)
        parts.extend([p for p in split if p])
    return [p.lower() for p in parts if p]


def to_snake_case(parts: Iterable[str]) -> str:
    return "_".join(parts)


def to_camel_case(parts: Iterable[str]) -> str:
    parts_list = list(parts)
    if not parts_list:
        return ""
    head, *tail = parts_list
    return head + "".join(p.capitalize() for p in tail)


def to_pascal_case(parts: Iterable[str]) -> str:
    return "".join(p.capitalize() for p in parts)


def generate_variants(name: str) -> Set[str]:
    parts = split_identifier_parts(name)
    variants: Set[str] = set()

    # Canonical forms
    snake = to_snake_case(parts)
    camel = to_camel_case(parts)
    pascal = to_pascal_case(parts)

    variants.add(name)  # original as-is
    variants.add(name.lower())
    variants.add(snake)
    variants.add(camel)
    variants.add(pascal)
    # Also add kebab for completeness
    variants.add("-".join(parts))

    # Special case: remove underscores and capitalize the following letter, preserving other casing
    # Example: "aboutSC_en" -> "aboutSCEn"
    def underscore_capitalize(s: str) -> str:
        result_chars: List[str] = []
        capitalize_next = False
        for ch in s:
            if ch == "_":
                capitalize_next = True
                continue
            if capitalize_next and ch.isalpha():
                result_chars.append(ch.upper())
            else:
                result_chars.append(ch)
            capitalize_next = False
        return "".join(result_chars)

    variants.add(underscore_capitalize(name))

    return {v for v in variants if v}


def find_asset_names(assets_path: Path) -> List[str]:
    names: Set[str] = set()
    for root, dirnames, filenames in os.walk(assets_path):
        base = os.path.basename(root)
        for suffix in ASSET_DIR_SUFFIXES:
            if base.endswith(suffix):
                names.add(base[: -len(suffix)])
                break
    return sorted(names)


def should_exclude_dir(dir_name: str) -> bool:
    return dir_name in EXCLUDE_DIR_NAMES


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except Exception:
        return False


def iter_project_files(root: Path, allowed_exts: Set[str], exclude_roots: Optional[Set[Path]] = None) -> Iterable[Path]:
    exclude_roots = exclude_roots or set()
    exclude_roots = {p.resolve() for p in exclude_roots}
    for current_root, dirnames, filenames in os.walk(root):
        current_root_path = Path(current_root).resolve()
        # Skip entire subtree if under any excluded root
        if any(is_under(current_root_path, ex) for ex in exclude_roots):
            dirnames[:] = []
            continue
        # In-place prune excluded directories for efficiency
        dirnames[:] = [d for d in dirnames if not should_exclude_dir(d)]
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext in allowed_exts:
                yield current_root_path / filename


def build_search_patterns(variants: Set[str]) -> List[Tuple[str, re.Pattern]]:
    patterns: List[Tuple[str, re.Pattern]] = []
    for variant in variants:
        # If variant looks like an identifier (letters/digits/_), use word boundary match
        if re.fullmatch(r"[A-Za-z0-9_]+", variant):
            pattern = re.compile(rf"\b{re.escape(variant)}\b")
        else:
            # Otherwise plain substring match via regex
            pattern = re.compile(re.escape(variant))
        patterns.append((variant, pattern))
    return patterns


def scan_usages(
    project_root: Path,
    asset_to_variants: Dict[str, Set[str]],
    allowed_exts: Set[str],
    exclude_roots: Optional[Set[Path]] = None,
) -> Dict[str, List[Tuple[Path, str, int, str]]]:
    """Scan files and return mapping of asset -> list of (file, variant, line_no, line_text)."""
    matches: Dict[str, List[Tuple[Path, str, int, str]]] = {k: [] for k in asset_to_variants}

    # Pre-compile patterns per asset
    compiled: Dict[str, List[Tuple[str, re.Pattern]]] = {
        name: build_search_patterns(variants) for name, variants in asset_to_variants.items()
    }

    for file_path in iter_project_files(project_root, allowed_exts, exclude_roots=exclude_roots):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            continue

        for asset_name, patterns in compiled.items():
            for line_no, line in enumerate(lines, start=1):
                for variant, regex in patterns:
                    if regex.search(line):
                        snippet = line.strip()
                        matches[asset_name].append((file_path, variant, line_no, snippet))
        # Continue scanning remaining files

    # Prune empty
    return {k: v for k, v in matches.items() if v}


def write_assets_list(output_path: Path, asset_to_variants: Dict[str, Set[str]]) -> None:
    lines: List[str] = []
    for name in sorted(asset_to_variants.keys()):
        variants_sorted = sorted(asset_to_variants[name])
        lines.append(f"{name}: {', '.join(variants_sorted)}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_unused_results(output_path: Path, all_assets: List[str], matches: Dict[str, List[Tuple[Path, str]]]) -> None:
    """Write only unused asset names (no matches for any variant)."""
    used: Set[str] = set(matches.keys())
    unused = [name for name in all_assets if name not in used]
    output_path.write_text("\n".join(unused) + ("\n" if unused else ""), encoding="utf-8")


def find_assets_directory(project_root: Path) -> Optional[Path]:
    """Find a directory named *.xcassets, preferring those ending with Assets.xcassets."""
    candidates: List[Path] = []
    for current_root, dirnames, filenames in os.walk(project_root):
        # prune excluded dirs
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_NAMES]
        for d in dirnames:
            if d.endswith(".xcassets"):
                candidates.append(Path(current_root) / d)
    if not candidates:
        return None
    # Prefer explicitly named Assets.xcassets, else the first sorted
    preferred = [p for p in candidates if p.name == "Assets.xcassets"]
    return sorted(preferred or candidates, key=lambda p: str(p))[0]


def scan_assets(
    assets_path: Path,
    project_root: Path,
    output_dir: Path,
    allowed_exts: Optional[Set[str]] = None
) -> Tuple[Path, Path, Path]:
    """
    Scan assets and write reports.
    Returns: (assets_list_path, unused_path, used_path)
    """
    if allowed_exts is None:
        allowed_exts = DEFAULT_SCAN_FILE_EXTENSIONS

    assets_list_path = output_dir / "assets_list.txt"
    result_path = output_dir / "result.txt"
    used_result_path = output_dir / "used_result.txt"

    if not assets_path.exists() or not assets_path.is_dir():
        raise ValueError(f"Assets directory not found: {assets_path}")

    asset_names = find_asset_names(assets_path)
    asset_to_variants: Dict[str, Set[str]] = {name: generate_variants(name) for name in asset_names}

    # Write full list with variants
    write_assets_list(assets_list_path, asset_to_variants)

    # Scan for usages
    matches = scan_usages(project_root, asset_to_variants, allowed_exts, exclude_roots={assets_path})

    # Write only UNUSED assets to result
    write_unused_results(result_path, asset_names, matches)

    # Write USED assets with locations, pretty formatted
    used_lines: List[str] = []
    for asset_name in sorted(matches.keys()):
        used_lines.append("".ljust(1))
        used_lines.append(f"=== Asset: {asset_name} ===")
        # Group by file
        file_groups: Dict[Path, List[Tuple[str, int, str]]] = {}
        for file_path, variant, line_no, snippet in matches[asset_name]:
            file_groups.setdefault(file_path, []).append((variant, line_no, snippet))
        for file_path in sorted(file_groups.keys(), key=lambda p: str(p)):
            used_lines.append(f"File: {file_path}")
            # Deduplicate variant/line pairs and sort
            seen: Set[Tuple[str, int, str]] = set(file_groups[file_path])
            for variant, line_no, snippet in sorted(seen, key=lambda x: (x[1], x[0])):
                truncated = (snippet[:200] + "…") if len(snippet) > 200 else snippet
                used_lines.append(f"  - L{line_no}: {variant} | {truncated}")
    used_result_path.write_text("\n".join(used_lines).lstrip() + ("\n" if used_lines else ""), encoding="utf-8")

    return assets_list_path, result_path, used_result_path
