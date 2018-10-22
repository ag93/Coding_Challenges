#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys, curr_level = 0, 0
    for step in s:
        if curr_level == 0 and step == 'D':
            num_valleys += 1
        if step == 'U':
            curr_level += 1
        else:
            curr_level -= 1
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()