#!/bin/bash

export PYTHONPATH=/usr/app/lib:${PYTHONPATH}

python3 loop.py ${INTERVAL:-1}
