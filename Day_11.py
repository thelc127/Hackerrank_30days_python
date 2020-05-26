#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
max_sum = -100
for i in range(0, 6):

    for j in range(0, 6):

        try:
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hg_sum = top + bottom + mid
            if (hg_sum > max_sum):
                max_sum = hg_sum
         
        except:
            continue
    
print (max_sum)
