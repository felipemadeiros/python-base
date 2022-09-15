#!/usr/bin/envi python3

import os, sys

path = os.path.join(os.curdir, "files")
filepath = os.path.join(path, "names2.txt")

# LBYL - Look Before You Leap
if os.path.exists(filepath):
    input("...") # Race Condition
    names = open(filepath).readlines()
else:
    print("[Error] File not found")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)