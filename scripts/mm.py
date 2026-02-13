#!/usr/bin/env python3
"""
MASTERMIND CLI — Commands to help the system improve all systems.

Usage:
  mm add "your idea here"     Add idea to Main Memory (New/Unprocessed)
  mm propagate                 Interactive propagation run
  mm check                     Validate system structure; totality check
  mm sync-links                Copy MASTERMIND_LINK to all project roots
  mm scan                      Show unprocessed ideas; propagation queue
  mm status                    Quick system status
  mm pre-publish               Audit before public push (paths, secrets)

Works with both mastermind/ (modular) and 888/ (workspace) layouts.
Detects root by searching for core/memory/main_memory.md or 888/memory/main_memory.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


def find_root() -> Path | None:
    """Find MASTERMIND or 888 root by walking up from cwd or script location."""
    script_dir = Path(__file__).resolve().parent
    for start in [Path.cwd(), script_dir.parent, script_dir.parent.parent]:
        p = start
        while True:
            if (p / "core" / "memory" / "main_memory.md").exists():
                return p
            if (p / "888" / "memory" / "main_memory.md").exists():
                return p
            if p == p.parent:
                break
            p = p.parent
    return None


def get_paths(root: Path) -> dict:
    """Return paths for core (modular) or 888 layout."""
    if (root / "core" / "memory" / "main_memory.md").exists():
        return {
            "main_memory": root / "core" / "memory" / "main_memory.md",
            "epiphanies": root / "core" / "memory" / "epiphanies.md",
            "session_log": root / "core" / "memory" / "session_log.md",
            "registry": root / "core" / "projects" / "_registry.md",
            "changelog": root / "core" / "CHANGELOG.md",
            "propagation": root / "core" / "processes" / "improvement_propagation.md",
            "link_template": root / "templates" / "MASTERMIND_LINK.md",
            "workspace": root.parent if "core" in str(root) else root,
        }
    # 888 layout
    return {
        "main_memory": root / "888" / "memory" / "main_memory.md",
        "epiphanies": root / "888" / "memory" / "epiphanies.md",
        "session_log": root / "888" / "memory" / "session_log.md",
        "registry": root / "888" / "projects" / "_registry.md",
        "changelog": root / "888" / "CHANGELOG.md",
        "propagation": root / "888" / "processes" / "improvement_propagation.md",
        "link_template": root / "888" / "sync" / "master_template.md",  # fallback
        "workspace": root,
    }


def cmd_add(root: Path, paths: dict, idea: str, source: str = "CLI") -> int:
    """Add idea to Main Memory New/Unprocessed."""
    mm = paths["main_memory"]
    content = mm.read_text(encoding="utf-8")
    date = datetime.now().strftime("%Y-%m-%d")
    new_row = f"| {date} | {idea} | {source} |"
    # Find New/Unprocessed table and append
    pattern = r"(\|\s*Added\s*\|\s*Entry\s*\|\s*Source\s*\|\n\|[-:\s|]+\|\n)((?:\|[^|]+\|[^|]+\|[^|]+\|\n)*)"
    match = re.search(pattern, content)
    if match:
        prefix, table = match.groups()
        if "| — | — | — |" in table:
            new_table = table.replace("| — | — | — |", f"| — | — | — |\n{new_row}")
        else:
            new_table = table.rstrip() + "\n" + new_row + "\n"
        content = content[: match.start()] + prefix + new_table + content[match.end() :]
    else:
        # Fallback: append before --- after New/Unprocessed
        insert = f"\n{new_row}\n"
        if "| — | — | — |" in content:
            content = content.replace("| — | — | — |", f"| — | — | — |\n{new_row}")
        else:
            content = content.replace(
                "*(Ideas added here have NOT yet",
                f"{new_row}\n\n*(Ideas added here have NOT yet",
            )
    mm.write_text(content, encoding="utf-8")
    print(f"[OK] Added to Main Memory: {idea[:60]}{'...' if len(idea) > 60 else ''}")
    print("  Run 'mm propagate' to evaluate and apply improvements.")
    return 0


def cmd_scan(root: Path, paths: dict) -> int:
    """Show unprocessed ideas and propagation queue."""
    mm = paths["main_memory"]
    content = mm.read_text(encoding="utf-8")
    # Find New/Unprocessed table rows (skip header and separator)
    in_table = False
    count = 0
    for line in content.splitlines():
        if "New / Unprocessed" in line:
            in_table = True
            continue
        if in_table and line.startswith("|") and "---" not in line and "Added" not in line:
            if "| — | — | — |" in line:
                continue
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 2:
                count += 1
                s = parts[1]
                print(f"  [{count}] {s[:70]}{'...' if len(s) > 70 else ''}")
        if in_table and line.strip().startswith("---"):
            break
    if count == 0:
        print("  No unprocessed ideas in Main Memory.")
    else:
        print(f"\n  → {count} idea(s) ready for propagation. Run 'mm propagate'.")
    return 0


def cmd_check(root: Path, paths: dict) -> int:
    """Validate system structure and run totality check."""
    errors = []
    for name, p in paths.items():
        if name in ("workspace", "link_template") and "888" in str(p):
            continue
        if p.suffix == ".md" and p.exists() is False:
            errors.append(f"Missing: {p}")
    if errors:
        print("Issues found:")
        for e in errors:
            print(f"  [--] {e}")
        return 1
    print("[OK] Structure validated. Required files present.")
    print("\nTotality check - Before finishing, ask:")
    print("  Who  - Did we serve the user and mission?")
    print("  What - Did we deliver and document?")
    print("  When - Did we move toward milestones?")
    print("  Where - Are we aligned with project/mission direction?")
    print("  Why  - Does this fit the mission?")
    print("  How  - Did we follow the process?")
    return 0


def parse_registry_projects(registry_path: Path, workspace: Path) -> list[tuple[str, Path]]:
    """Parse project paths from _registry.md. Returns [(name, path), ...]."""
    if not registry_path.exists():
        return []
    content = registry_path.read_text(encoding="utf-8")
    projects = []
    in_table = False
    for line in content.splitlines():
        if "Project Map" in line or "| Project |" in line:
            in_table = True
            continue
        if in_table and line.strip().startswith("---"):
            break
        if not in_table or not line.strip().startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 2:
            name = parts[0].strip("**").strip()
            path_str = parts[1].strip()
            if path_str and path_str != "Path" and not path_str.startswith("(") and not path_str.startswith("-"):
                # Take first path if comma-separated (e.g. "path/A, path/B")
                path_str = path_str.split(",")[0].strip()
                proj_path = (workspace / path_str).resolve()
                projects.append((name, proj_path))
    return projects


def cmd_sync_links(root: Path, paths: dict) -> int:
    """Copy MASTERMIND_LINK to all project roots from registry."""
    workspace = paths["workspace"]
    registry = paths["registry"]
    projects = parse_registry_projects(registry, workspace)
    # For 888, link template might be different - use a generated one
    link_content = """# MASTERMIND Link

**This project is part of the coordination system.**

- **Central control:** mastermind.md (workspace root)
- **Engine:** {engine_path}/
- **Registry:** {registry_path}

When coordinating, read mastermind.md first.
"""
    engine_path = "888" if (root / "888").exists() else "mastermind/core"
    registry_path = "888/projects/_registry.md" if (root / "888").exists() else "mastermind/core/projects/_registry.md"
    link_content = link_content.format(engine_path=engine_path, registry_path=registry_path)
    if not projects:
        print("No projects found in registry. Configure core/projects/_registry.md (or 888/projects/).")
        return 0
    for name, proj_path in projects:
        if proj_path.exists():
            link_file = proj_path / "MASTERMIND_LINK.md"
            link_file.write_text(link_content, encoding="utf-8")
            print(f"  [OK] {name}: {link_file}")
        else:
            print(f"  [--] {name}: path not found ({proj_path})")
    return 0


def cmd_propagate(root: Path, paths: dict) -> int:
    """Interactive propagation guide."""
    proc = paths["propagation"]
    if not proc.exists():
        print("Propagation process file not found.")
        return 1
    print("=" * 60)
    print("IMPROVEMENT PROPAGATION — Guided Run")
    print("=" * 60)
    print("\n1. Read Main Memory and list ideas to evaluate.")
    print(f"   File: {paths['main_memory']}")
    print("\n2. For each idea, evaluate against each project (see registry).")
    print(f"   Registry: {paths['registry']}")
    print("\n3. Apply improvements where they fit. Document in CHANGELOG.")
    print("\n4. Propagate: Does this improvement apply elsewhere? Apply there.")
    print("\n5. Document: session_log, main_memory (move from New), CHANGELOG.")
    print("\n6. Totality check: Who? What? When? Where? Why? How?")
    print("\n" + "=" * 60)
    print(f"Full process: {proc}")
    print("=" * 60)
    return 0


def cmd_pre_publish(root: Path, paths: dict) -> int:
    """Pre-publish audit: check structure, scan for private content."""
    issues = []
    # 1. Run structure check
    if cmd_check(root, paths) != 0:
        issues.append("Structure check failed")
    # 2. Find mastermind folder to scan (modular copy)
    mastermind_dir = root / "mastermind" if (root / "mastermind" / "core").exists() else root
    if not (mastermind_dir / "core").exists():
        mastermind_dir = root  # might be mastermind itself
    # 3. Scan for workspace-specific paths
    exclude_names = {"mm.py"}  # Scanner contains detection pattern; skip self
    for ext in [".md", ".py", ".bat", ".sh", ".ps1"]:
        for f in mastermind_dir.rglob(f"*{ext}"):
            if "node_modules" in str(f) or ".git" in str(f) or f.name in exclude_names:
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                rel = f.relative_to(mastermind_dir)
                if "d:\\Workspace" in text or "d:/Workspace" in text or "d:\\\\Workspace" in text:
                    issues.append(f"{rel}: contains workspace path")
                # Stripe live key (key format: sk_live_ followed by 24+ chars)
                if "sk_live_" in text and re.search(r"sk_live_[a-zA-Z0-9]{24,}", text):
                    issues.append(f"{rel}: possible Stripe live key")
            except Exception:
                pass
    # 4. Report
    print("\n" + "=" * 50)
    print("PRE-PUBLISH AUDIT")
    print("=" * 50)
    if not issues:
        print("[OK] No private content detected.")
        print("[OK] Run 'mm check' for structure. You're ready to push.")
        return 0
    print("[!!] Issues to review:")
    for i in issues:
        print(f"  - {i}")
    print("\nFix these before making the repo public.")
    return 1


def cmd_status(root: Path, paths: dict) -> int:
    """Quick system status."""
    layout = "888" if (root / "888").exists() else "mastermind (modular)"
    print(f"Layout: {layout}")
    print(f"Root: {root}")
    print(f"Main Memory: {paths['main_memory']}")
    cmd_scan(root, paths)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="MASTERMIND CLI — A system that improves all systems.",
        epilog="By David Edward Sproule & Cursor AI",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="Quick system status")
    sub.add_parser("pre-publish", help="Audit before public push")
    sub.add_parser("scan", help="Show unprocessed ideas")
    sub.add_parser("check", help="Validate structure; totality check")
    sub.add_parser("propagate", help="Interactive propagation guide")
    sub.add_parser("sync-links", help="Copy MASTERMIND_LINK to project roots")
    add_p = sub.add_parser("add", help="Add idea to Main Memory")
    add_p.add_argument("idea", help="The idea to add")
    add_p.add_argument("-s", "--source", default="CLI", help="Source (default: CLI)")
    args = parser.parse_args()
    root = find_root()
    if not root:
        print("MASTERMIND root not found. Run from within a workspace containing mastermind/ or 888/.")
        return 1
    paths = get_paths(root)
    if args.cmd == "add":
        return cmd_add(root, paths, args.idea, getattr(args, "source", "CLI"))
    if args.cmd == "scan":
        return cmd_scan(root, paths)
    if args.cmd == "check":
        return cmd_check(root, paths)
    if args.cmd == "propagate":
        return cmd_propagate(root, paths)
    if args.cmd == "sync-links":
        return cmd_sync_links(root, paths)
    if args.cmd == "status":
        return cmd_status(root, paths)
    if args.cmd == "pre-publish":
        return cmd_pre_publish(root, paths)
    return 0


if __name__ == "__main__":
    sys.exit(main())
