#!/usr/bin/python

import sys

count = 0
oldKey = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count
        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += 1

if oldKey != None:
    print oldKey, "\t", count

