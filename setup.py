#!/usr/bin/env python

import os
import sys
from pathlib import Path
from subprocess import Popen, PIPE

from setuptools import setup

MODULE_NAME = 'fact_helper_file'
MIME_DIR = Path(__file__).parent / MODULE_NAME / 'mime'


class OperateInDirectory:
    def __init__(self, target_directory: str):
        self._current_working_dir = None
        self._target_directory = target_directory

    def __enter__(self):
        self._current_working_dir = os.getcwd()
        os.chdir(self._target_directory)

    def __exit__(self, *_):
        os.chdir(self._current_working_dir)


def execute_shell_command(shell_command):
    with Popen(shell_command, shell=True, stdout=PIPE, stderr=PIPE) as pl:
        output = pl.communicate()[0].decode('utf-8', errors='replace')
        return output, pl.returncode


os.makedirs(str(MIME_DIR.parent / 'bin'), exist_ok=True)
with OperateInDirectory(str(MIME_DIR)):
    FILE_OUTPUT, FILE_CODE = execute_shell_command(
        '(cat custom_* > custommime)'
        ' && file -C -m custommime'
        ' && mv -f custommime.mgc ../bin/'
        ' && rm custommime'
    )
    if FILE_CODE != 0:
        sys.exit('Failed to properly compile magic file\n{}'.format(FILE_OUTPUT))


setup(
    name=MODULE_NAME,
    version='0.2.7',
    description='Helper functions for file type generation',
    author='Johannes vom Dorp',
    url='https://github.com/fkie-cad/fact_helper_file',
    install_requires=['python-magic'],
    python_requires='>=3.5',
    packages=[MODULE_NAME, ],
    package_data={MODULE_NAME: [str(MIME_DIR.parent / 'bin' / 'custommime.mgc'), ]}
)
