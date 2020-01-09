#!/bin/python3

import math
import os
import random
import re
import sys
import ripdb

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat1 = x
    cat2 = y
    mouse = z

    dist1 = abs(mouse - cat1)
    dist2 = abs(mouse - cat2)


    if dist1 == dist2:
        return 'Mouse C'
    elif dist1 < dist2:
        return 'Cat A'
    else:
        return 'Cat B'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        #fptr.write(result + '\n')
        print(result)

    #fptr.close()
