# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:40:07 2019

@author: emirhan
"""

#!/bin/python3

# Complete the minimumBribes function below.
def minimumBribes(q):
    Q=[P-1 for P in q]
    bribe=0
    for i,j in enumerate(Q):
        if j>(i)+2:
            print('Too chaotic')
            return
        else:
#            print(Q)
#            print((max(j-1,0),i))
            for k in range(max(j-1,0),i):
                if q[k]>j:
                    bribe+=1

    print(bribe)
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
