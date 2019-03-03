#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary = 0
secondary = 0
for d_i in range(n):
    primary += a[d_i][d_i]
    secondary += a[n - d_i - 1][d_i]

diff = abs(primary - secondary)
print(diff)
