#!/usr/bin/env python

import subprocess


subprocess.run(["git", "init"])
subprocess.run(["poetry", "install"])
subprocess.run(["poetry", "run", "pre-commit", "install", "--install-hooks", "-t", "pre-commit", "-t", "commit-msg"])
subprocess.run(["poetry", "run", "pre-commit", "autoupdate"])
