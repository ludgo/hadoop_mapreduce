#!/usr/bin/python

import sys

salesTotal = 0
total = []
oldKey = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        total.append(salesTotal)
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    total.append(salesTotal)
    print oldKey, "\t", salesTotal

count = 0.0
for ammount in total:
    count += ammount

print count

