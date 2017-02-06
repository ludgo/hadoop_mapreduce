#!/usr/bin/python

import sys

count = 0
oldKey = None

maxVal = 0
maxKey = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        if count > maxVal:
            maxVal = count
            maxKey = oldKey

        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += 1

if oldKey != None:
    if count > maxVal:
        maxVal = count
        maxKey = oldKey

if maxKey != None:
    print maxKey, "\t", maxVal
