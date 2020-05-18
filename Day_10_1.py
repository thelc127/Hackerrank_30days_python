#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    def decimaltoBinar(n):
        if n > 1:
            decimaltoBinar( n // 2)
            return  n % 2

    m1 = decimaltoBinar()
    m2 = m1.split()
    if 
