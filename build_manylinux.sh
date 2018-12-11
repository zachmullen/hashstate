#!/bin/bash
#   docker build -t manylinux .
#   docker run -v $(pwd)/dist:/dist manylinux
set -e

for V in cp34-cp34m cp35-cp35m cp36-cp36m
do
  PATH=/opt/python/$V/bin:$PATH python setup.py bdist_wheel
done
