# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:49:39 2019

@author: Matt
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)
   
    
print(recurPower(2, 6))
