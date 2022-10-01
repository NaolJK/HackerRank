#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    step = 0
    is_going_up = False
    is_going_down = False

    valley = 0
    for i in range(0, steps):
        if path[i] == "U":
            step += 1
            is_going_down = False
            is_going_up = True
        if path[i] == "D":
            step -= 1
            is_going_down = True
            is_going_up = False
        if is_going_up and step == 0:
            valley += 1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
