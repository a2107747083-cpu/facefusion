#!/usr/bin/env python3
"""Windows desktop entry for FaceFusion packaged app."""

from __future__ import annotations

import os
import sys
from tkinter import Tk, messagebox

os.environ['OMP_NUM_THREADS'] = '1'

from facefusion import conda, core


def show_brand_popup() -> None:
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showinfo('FaceFusion', '荀彧制造 假一赔十', parent=root)
    root.destroy()


def main() -> None:
    show_brand_popup()
    conda.setup()

    if len(sys.argv) == 1:
        sys.argv.extend(['run'])

    core.cli()


if __name__ == '__main__':
    main()
