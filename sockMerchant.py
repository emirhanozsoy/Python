# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:38:26 2019

@author: emirhan
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    number_of_pairs=0
    i=0
    j=1
    lenght=len(ar)
    while i<len(ar):
        if i>=lenght:
                break
        while True:
            if j>=lenght:
                break
            print(number_of_pairs)
            #print(i,j,ar[i],ar[j])
            if i >= j:
                j=j+1
            elif ar[i]==ar[j]:
                print('**')
                number_of_pairs=number_of_pairs+1
                print(i,j)
                print(ar)
                ar.pop(j)
                print(ar)
                ar.pop(i)
                j=0
                lenght=lenght-2
            print(j,lenght) 
            j=j+1
            if j>=lenght:
                j=0
                break
        i=i+1
        j=i+1
    return number_of_pairs
            

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

#    fptr.write(str(result) + '\n')
#
#    fptr.close()
    print(result)
