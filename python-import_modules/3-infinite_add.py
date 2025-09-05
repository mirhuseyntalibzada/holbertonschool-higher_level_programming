#!/usr/bin/python3

import sys

argv_sum = 0

for i in range(1, len(sys.argv)):
    argv_sum += int(sys.argv[i])

print("{}".format(argv_sum))
