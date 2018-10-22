#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp = []
    temp.append(ar[0])
    for i in range(1,n):
        if ar[i] in temp:
            temp.remove(ar[i])
        else:
            temp.append(ar[i])
    return (n - len(temp)) // 2




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()