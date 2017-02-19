#!/usr/bin/python

import sys

wordIds = []
oldWord = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue
    
    thisWord, nodeid = data_mapped

    if oldWord and oldWord != thisWord:
        if len(wordIds) > 0:
            print('{0}\t{1}\t{2}'.format(oldWord, len(wordIds), ','.join(wordIds)))
        oldWord = thisWord;
        wordIds = []

    oldWord = thisWord
    wordIds.append(nodeid)

if oldWord != None:
    print('{0}\t{1}\t{2}'.format(oldWord, len(wordIds), ','.join(wordIds)))

