#!/usr/bin/python

import sys

for line in sys.stdin:

    data = line.strip().split()

    if len(data) == 10:

        ipaddress, identity, username, servertime, zone, requestmethod, requestpath, requestprotocol, statuscode, size = data
        print requestpath

