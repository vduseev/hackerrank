#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positives = 0
negatives = 0
zeroes = 0
for i in range(n):
    if arr[i] < 0:
        negatives += 1
    elif arr[i] == 0:
        zeroes += 1
    else:
        positives += 1

print(positives / n)
print(negatives / n)
print(zeroes / n)