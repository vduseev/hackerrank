#!/bin/python3

import sys


n = int(input().strip())
heights = [int(height_temp) for height_temp in input().strip().split(' ')]

max_height = max(heights)
tallest_candles = list(filter(lambda x: x == max_height, heights))
print(len(tallest_candles))