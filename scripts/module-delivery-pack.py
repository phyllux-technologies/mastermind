#!/usr/bin/env python3
"""
Generate a delivery-ready module ZIP with optional personalization.

Usage:
  python scripts/module-delivery-pack.py quality-hierarchy
  python scripts/module-delivery-pack.py quality-hierarchy --email buyer@example.com --order 123456

Without --email: Uses standard LICENSE.txt from module folder.
With --email: Injects "Licensed to: email" and "Order: XXX" into generated LICENSE.txt.

Output: modules/quality-hierarchy-delivery.zip (or similar)
"""

import argparse
import zipfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Pack module for delivery")
    parser.add_argument("module", help="Module name (e.g. quality-hierarchy)")
    parser.add_argument("--email", help="Purchaser email (for personalization)")
    parser.add_argument("--order", help="Order/transaction ID (last 6 digits)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    module_dir = root / "modules" / args.module
    if not module_dir.exists():
        print(f"Error: {module_dir} not found")
        return 1

    out_name = f"{args.module}-delivery.zip"
    out_path = root / "modules" / out_name

    license_content = (module_dir / "LICENSE.txt").read_text(encoding="utf-8")
    if args.email or args.order:
        extra = [
            "This copy is licensed to the purchaser named below.",
            "Unauthorized distribution can be traced to the original purchaser.",
            "",
        ]
        if args.email:
            extra.append(f"Licensed to: {args.email}")
        if args.order:
            extra.append(f"Purchase ID: ...{str(args.order)[-6:]}")
        extra.append("")
        license_content = "\n".join(extra) + license_content

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in module_dir.rglob("*"):
            if f.is_dir() or f.name.endswith("-delivery.zip"):
                continue
            arcname = f.relative_to(module_dir)
            if args.email or args.order:
                if f.name == "LICENSE.txt":
                    zf.writestr(str(arcname), license_content)
                    continue
            zf.write(f, arcname)

    print(f"Created: {out_path}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
