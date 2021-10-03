#!/usr/bin/env python

import os
import subprocess
from tempfile import gettempdir


subprocess.run(["git", "init"])
if not os.getcwd().startswith(os.path.realpath(gettempdir())):
    subprocess.run(["poetry", "install"])
    subprocess.run(["poetry", "run", "pre-commit", "install", "-t", "pre-commit", "-t", "commit-msg"])
    subprocess.run(["poetry", "run", "pre-commit", "autoupdate"])
