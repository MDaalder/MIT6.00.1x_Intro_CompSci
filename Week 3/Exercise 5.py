# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:01:51 2019

@author: Matt
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, halve, max], -3))
