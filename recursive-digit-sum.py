#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    num = 0
    for ch in n:
        num += int(ch)

    return recursiv_super_digit(str(num * k))
    
def recursiv_super_digit(n):
    if len(n) == 1:
        return int(n)
    
    num = 0
    for ch in n:
        num += int(ch)
        
    return recursiv_super_digit(str(num))
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
