#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0;
    for i in range (0,len(a)):
        for j in range (0, len(a)-1):
            if a[j]> a[j+1]:
               swaps = swaps + 1
               temp = a[j]
               a[j] = a[j+1]
               a[j+1] = temp
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
