#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    is_p_odd = p % 2 != 0

    if p == 1:
        return 0

    if n % 2 == 0 and p == n:
        return 0

    if n % 2 != 0 and p in [n, n-1]:
        return 0

    total_possible_flips = int(n / 2)
    flips_from_start = int(p / 2) 
    flips_from_back = total_possible_flips - flips_from_start
   
    return min(flips_from_start, flips_from_back)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
