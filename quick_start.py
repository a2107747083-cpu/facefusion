#!/usr/bin/env python3
"""Windows double-click starter for FaceFusion.

Features:
- checks Python version
- installs requirements
- starts main program
- opens browser automatically
- writes error.log on failure
"""

from __future__ import annotations

import os
import subprocess
import sys
import traceback
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ERROR_LOG = ROOT / 'error.log'
URL = 'http://127.0.0.1:7860'


def log_error(message: str) -> None:
    ERROR_LOG.write_text(message, encoding='utf-8')


def run_command(cmd: list[str]) -> None:
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        raise RuntimeError(f"命令执行失败({result.returncode}): {' '.join(cmd)}")


def ensure_python() -> None:
    if sys.version_info < (3, 10):
        raise RuntimeError('需要 Python 3.10 或更高版本。')


def install_requirements() -> None:
    run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    run_command([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])


def start_program() -> None:
    webbrowser.open(URL)
    run_command([sys.executable, 'facefusion.py', 'run'])


def main() -> int:
    try:
        if ERROR_LOG.exists():
            ERROR_LOG.unlink()

        os.environ.setdefault('OMP_NUM_THREADS', '1')
        ensure_python()
        install_requirements()
        start_program()
        return 0
    except Exception as exc:  # noqa: BLE001
        detail = [
            'FaceFusion 启动失败。',
            f'错误: {exc}',
            '',
            '详细堆栈:',
            traceback.format_exc(),
        ]
        log_error('\n'.join(detail))
        print('\n启动失败，详情已写入 error.log')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
