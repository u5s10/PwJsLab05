#!/usr/bin/python
import sys
from pathlib import Path
import os

def isCopy(file1, file2):
    f1_size = Path(file1).stat().st_size
    f2_size = Path(file2).stat().st_size
    
    if f1_size != f2_size:
        return 0

    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while 1:
            byte_s1 = f1.read(1)
            byte_s2 = f2.read(1)
            if not byte_s1 and not byte_s2:
                break;
            byte_1 = byte_s1[0]
            byte_2 = byte_s2[0]
            if byte_1 != byte_2:
                return 0
        return f1_size


def getAllFiles(baseDir, allFiles):
    outPut = allFiles
    bd = baseDir
    for entry in os.listdir(bd):
        if os.path.isfile(os.path.join(bd, entry)):
            outPut.append(os.path.join(bd, entry))
        elif os.path.isdir(os.path.join(bd, entry)):
            getAllFiles(os.path.join(bd,entry), outPut)
    return outPut


count = 0
files = []
lst = []

for i in range(0,len(sys.argv)):
    if i == 0:
        continue
    lst = []
    files += getAllFiles(sys.argv[i],lst)

seen = []
out = []
dupsize = 0
for i in files:
    seen.append(i)
    for j in files:
        if j in seen:
            continue
        size = isCopy(i,j)
        if size > 0:
            out.append(i)
            out.append(j)
            dupsize += size

print('duplicated: (size: {0}b)'.format(dupsize))
out = list(set(out))

for i in out:
    print(i)
