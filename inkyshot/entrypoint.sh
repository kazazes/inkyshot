#!/bin/bash

set -ex

export PYTHONPATH=/opt/waveshare-sdk/python/lib:${PYTHONPATH}

/usr/app/waveshare-display/display.py -i /usr/app/images/lords.jpg

balena-idle
