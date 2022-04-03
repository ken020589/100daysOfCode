##!/usr/bin/env python
#day4 Array

import numpy as np
x = np.array([3,6,9,12,15,18])
y = np.array([2,4,8,16,32,64])
print(x+y)
print(x*y)

print(x[0]) # index is start from 0
print(x[-1]) #the last element
print(x[0:2]) # x[0] & x[1]
print(x[:4]) # x[0] to x[3]
print(x[3:]) # x[3] to x[4]
print(x[:]) # print all elements

z = np.reshape(x,(2,-1))
print(z)
print(z[0,2])

y = np.arange(5,35,7)
print(y)

a = np.ones((2,3,4), dtype=np.int16)
print(a)