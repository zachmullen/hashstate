#!/bin/bash
set -e

for V in cp34-cp34m cp35-cp35m cp36-cp36m
do
  PATH=/opt/python/$V/bin:$PATH python setup.py bdist_wheel
done

for whl in dist/*-linux_*.whl
do
  auditwheel repair "$whl" -w dist/
  rm "$whl"
done
