# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:42:24 2019

@author: Matt

myLog(x, b) Computes the logarithm of a number x relative to a base b.

i.e. if x = 16, b = 2, result is 4 because 2^4 = 16
i.e. if x = 15, b = 3, result is 2 because 3^2 is the largest power of 3 less than 15

So: b^result <= x

x and b are positive integers; b is an integer greater than or equal to 2.
Function returns an integer answer.

x: a positive integer
b: a positive integer; b >= 2

returns: log_b(x), or, the logarithm of x relative to a base b.
"""

def myLog(x, b):
    
       
    result = 0
    while b**result <= x:
        result += 1
        if b**result > x:
            return (result - 1)
            
    return result
    
        
    
x = 6
b = 2
print(myLog(x, b))