# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:54:09 2019

@author: emirh
"""

#!/bin/python3

import sys

M = 1000000007

n, m = map(int, input().split())
mm = pow(2, m, M) - 1

if mm < n:
    print(0)
    sys.exit(0)

modinv = [-1 for _ in range(n + 1)]
modinv[1] = 1
for x in range(2, n + 1):
    modinv[x] = (-(M//x) * modinv[M%x])%M

choose = mm

f = [1, 0]
for k in range(2, n + 1):
    res = (choose - f[-2]*(mm - (k - 2)) - f[-1])%M
    if k > mm:
        choose = 0
    else:
        choose = (choose * (mm - k + 1) * modinv[k]) % M
    f.append((res*modinv[k]) % M)
    del f[0]

fact = 1
for i in range(1, n + 1):
    fact *= i
    fact %= M
print(((choose - f[-1])*fact)%M)