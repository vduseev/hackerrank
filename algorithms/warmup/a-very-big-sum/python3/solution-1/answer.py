#!/bin/python3
# Tad: python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
summary = sum(arr)
print(summary)
