#!/bin/bash

set -ex
export PYTHONPATH=/app/lib:${PYTHONPATH}

python3 display.py -i img/bible.jpeg
balena-idle
