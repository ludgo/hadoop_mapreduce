#!/usr/bin/python

import sys, csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:

	if len(line) == 19:
		
		nodeid = line[0]
		body = re.split('[ .,!?:;"()<>\[\]#$=\-/]', line[4])

		for word in body:
			print('{0}\t{1}'.format(word.lower(), nodeid))

