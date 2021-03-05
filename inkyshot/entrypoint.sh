#!/bin/bash

set -ex

export PYTHONPATH=/opt/waveshare-sdk/python/lib:${PYTHONPATH}

IMG_URL=${IMG_URL:-'https://carolineliebert.files.wordpress.com/2011/03/lords_prayer.jpg'}

wget -O /tmp/image $IMG_URL

python3 /usr/app/waveshare-display/display.py -i /tmp/image

balena-idle
