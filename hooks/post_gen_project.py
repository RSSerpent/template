#!/usr/bin/env python

import os


os.system("git init")
os.system("poetry install")
os.system("poetry run pre-commit install")
os.system("poetry run pre-commit autoupdate")
