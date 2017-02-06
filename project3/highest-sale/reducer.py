#!/usr/bin/python

import sys

highest = 0
oldKey = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highest
        oldKey = thisKey;
        highest = 0

    oldKey = thisKey
    if float(thisSale) > highest:
        highest = float(thisSale)

if oldKey != None:
    print oldKey, "\t", highest

