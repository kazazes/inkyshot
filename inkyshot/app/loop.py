#!/usr/bin/env python3
from datetime import datetime, timedelta
import os
import subprocess
import time
import sys
import re

libdir = os.path.abspath("/usr/app/lib")
if os.path.exists(libdir):
    sys.path.append(libdir)

imagelist = []
imagedir = os.listdir("/usr/app/img")
for file in imagedir:
    extensionsToCheck = ('.jpeg', '.jpg', '.svg')

    if file.endswith(extensionsToCheck):
        imagelist.append({"filename": file, "fuzz": None})

print(imagelist)
interval = 5  # mins
if sys.argv[1]:
    interval = int(sys.argv[1])

print("Using " + str(interval) + " min. interval")


def run_cmd(cmdline):
    convert = subprocess.Popen(
        cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = convert.communicate()
    if len(stderr) > 1:
        print(stderr)
    return stdout.decode("UTF-8")


while True:
    item = imagelist.pop()
    imagelist.insert(0, item)

    cmdline = ["./display.py", "-i", item["filename"]]

    if item["fuzz"]:
        cmdline.append("-f")
        cmdline.append(f"{str(item['fuzz'])}")

    print(item["filename"])
    print(cmdline)
    run_cmd(cmdline)

    dt = datetime.now() + timedelta(minutes=interval)
    while datetime.now() < dt:
        time.sleep(30)
