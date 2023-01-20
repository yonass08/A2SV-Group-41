#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n-1
    last = arr[i]
    while (i > 0):
        if (arr[i-1] > last):
            arr[i] = arr[i-1]
            print(*arr)
            i = i-1
        else:
            arr[i] = last
            print(*arr)
            break
        
        
    
    if(i == 0):
        arr[0] = last
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
