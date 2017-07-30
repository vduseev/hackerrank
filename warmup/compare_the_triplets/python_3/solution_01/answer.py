#!/bin/python3

import sys


def solve(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]


a0, a1, a2 = input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]
result = solve(a, b)
print(" ".join(map(str, result)))
