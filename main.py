"""Copy the pre-rendered news infographic to the output directory.

Entry for make.fun bounty "news-image-20261123" (23 Nov 2026 world news
in one image). The image is pre-rendered (see render.py in the bounty
workspace, not part of this repo); this program only copies it,
byte for byte, to the output path. Standard library only, no network,
no image processing, fully deterministic.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / "entry.png"
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
