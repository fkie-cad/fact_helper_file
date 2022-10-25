#!/usr/bin/env python
from __future__ import annotations

import os
import sys
from pathlib import Path
from subprocess import run, STDOUT

from setuptools import setup

MODULE_NAME = 'fact_helper_file'
MODULE_DIR = Path(__file__).parent / MODULE_NAME
MIME_DIR = MODULE_DIR / 'mime'
BIN_DIR = MODULE_DIR / 'bin'


class OperateInDirectory:
    def __init__(self, target_directory: str | Path):
        self._current_working_dir = None
        self._target_directory = target_directory

    def __enter__(self):
        self._current_working_dir = Path.cwd()
        os.chdir(self._target_directory)

    def __exit__(self, *_):
        os.chdir(self._current_working_dir)


BIN_DIR.mkdir(exist_ok=True)

with OperateInDirectory(MIME_DIR):
    process = run(
        '(cat custom_* > custommime)'
        ' && file -C -m custommime'
        ' && mv -f custommime.mgc ../bin/'
        ' && rm custommime',
        shell=True,
        stderr=STDOUT,
    )
    if process.returncode != 0:
        sys.stderr.write(f'Failed to properly compile magic file\n{process.stdout}\n')
        sys.exit(1)


setup()
