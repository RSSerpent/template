#!/usr/bin/env python

import os
import subprocess
from tempfile import gettempdir


subprocess.run(["git", "init"])
curdir = os.path.normcase(os.getcwd())
tmpdir = os.path.normcase(os.path.realpath(gettempdir()))
if not curdir.startswith(tmpdir):
    subprocess.run(["poetry", "install"])
    subprocess.run(["poetry", "run", "pre-commit", "install", "-t", "pre-commit", "-t", "commit-msg"])
