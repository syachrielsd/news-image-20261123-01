#!/usr/bin/env python3
"""main.py — copy-only entrypoint for news-image-20261123-01.

Copies the pre-rendered entry.png (built at build time by render.py and
committed to this repo) to $MAKEFUN_OUTPUT_DIR/entry.png. It never renders.
The source path is resolved from this file's own directory, never from the
process working directory, so it works when run from any cwd.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst)


if __name__ == "__main__":
    main()
