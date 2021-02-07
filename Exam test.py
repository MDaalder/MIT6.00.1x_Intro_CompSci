# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:08:25 2019

@author: Matt
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(0.5))
        