#!/bin/python

import sys

inp = input().strip().split(' ')
a = []
for number in inp:
    a.append(int(number))

asc = sorted(a)
min_sum = sum(asc[:len(asc) - 1])
max_sum = sum(asc[1:])

print(min_sum, max_sum)