#!/bin/bash

# For pre-commit to work
# Ref: https://github.com/gitpod-io/gitpod/issues/1997
echo "export PIP_USER=false" >> ~/.bashrc

# Set up pre-commit
python3.8 -m pip install --user pre-commit
pre-commit install
pre-commit autoupdate # Not for prod. Need to reinstall if there's diff
