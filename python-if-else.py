#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0 or (n % 2 == 0 and (n<21 and n>5)):
    print("Weird")
# elif (n % 2 == 0 and n in [2,6]) or n>20 :
#     print("Not Weird")
# elif n%2 == 0 and n in [6,21]:
#     print("Weird")
else:
    print("Not Weird")

