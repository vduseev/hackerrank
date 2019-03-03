#!/bin/python3

import sys


n = int(input().strip())
for i in range(n):
    line = ''.join([' ' for x in range(n - i - 1)]) + ''.join(['#' for x in range(i + 1)])
    print(line)