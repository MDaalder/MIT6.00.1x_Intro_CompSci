# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:47:58 2019

@author: Matt
"""

testList = [1, -4, 8, -9]
# final value = [2, -3, 9, -8]

def addOne(a):
    return (a+1)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

    print(testList)

applyToEach(testList, addOne)


