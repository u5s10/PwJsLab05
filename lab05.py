#!/usr/bin/python
import sys
import argparse
from pathlib import Path
import os
import time


def bin_rep(file):
    f1_size = Path(file).stat().st_size
    bin_rep = ""
    with open(file, "rb") as f:
        bin_rep = str(f.read())
            
    return bin_rep


def get_all_files(baseDir, allFiles):
    outPut = allFiles
    bd = baseDir
    for entry in os.listdir(bd):
        if os.path.isfile(os.path.join(bd, entry)):
            outPut.append(os.path.join(bd, entry))
        elif os.path.isdir(os.path.join(bd, entry)):
            get_all_files(os.path.join(bd, entry), outPut)
    return outPut

files = []
for i in range(0, len(sys.argv)):
    if i == 0:
        continue
    lst = []
    files += get_all_files(sys.argv[i], lst)

files_dict = {}
for i in files:
    bin = bin_rep(i)
    if bin in files_dict:
        files_dict[bin].append(i)
    else:
        files_dict[bin] = [i]

for key in files_dict:
    if len(files_dict[key]) > 1:
        f_size = Path(files_dict[key][0]).stat().st_size*len(files_dict[key]) - 1
        if f_size < 0:
            continue
        print(f'duplicated: (size: {f_size}b)')
        for i in files_dict[key]:
            print(i)
        print()

