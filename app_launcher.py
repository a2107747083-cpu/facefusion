#!/usr/bin/env python3
"""Simple launcher to install and run FaceFusion as a local app."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run_cmd(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT).returncode


def ensure_python() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("需要 Python 3.10+ 才能运行该应用。")


def setup_env() -> int:
    ensure_python()

    pip = shutil.which("pip") or shutil.which("pip3")
    if not pip:
        print("未找到 pip，请先安装 Python 与 pip。")
        return 1

    code = run_cmd([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    if code != 0:
        return code

    code = run_cmd([sys.executable, "install.py"])
    return code


def launch_ui(headless: bool = False) -> int:
    ensure_python()
    command = [sys.executable, "facefusion.py", "headless-run" if headless else "run"]
    return run_cmd(command)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="FaceFusion 一键安装与启动器")
    parser.add_argument(
        "action",
        choices=["setup", "run", "headless", "all"],
        help="setup=安装依赖, run=启动界面, headless=无界面启动, all=先安装再启动",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.action == "setup":
        return setup_env()
    if args.action == "run":
        return launch_ui(False)
    if args.action == "headless":
        return launch_ui(True)

    code = setup_env()
    if code != 0:
        return code
    return launch_ui(False)


if __name__ == "__main__":
    raise SystemExit(main())
