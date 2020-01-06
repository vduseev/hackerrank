#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    is_in_valley=False
    valley_count=0

    for i in range(n):
        prev_level=level

        if s[i] == 'D':
            level-=1
        elif s[i] == 'U':
            level+=1
        
        if prev_level == 0 and level < 0:
            is_in_valley = True
        elif prev_level == -1 and level == 0:
            if is_in_valley:
                valley_count += 1
            is_in_valley = False

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
    #print(result)
