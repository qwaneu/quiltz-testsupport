#!/bin/bash
set -e
python -m venv venv
./run_tests.sh
pip install -r requirements/build.txt
python setup.py sdist bdist_wheel