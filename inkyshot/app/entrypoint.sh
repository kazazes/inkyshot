#!/bin/bash

set -ex
export PYTHONPATH=/app/lib:${PYTHONPATH}

python3 loop.py ${INTERVAL:-1}
