# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:14:24 2019

@author: Matt
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    example
    
    general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because
    1*10^3 + 2*10^2 + 3*10^1 + 4*10^0
    """
    
    def functionPoly(x):
        
        result = 0
        
        for n in range(len(L)):
            k = len(L) - 1
            iteration = L[n] * x**(k-n)
            #print(iteration)
            result += iteration
            #print(result)
            
        return result
        
        
    # will return a FUNCTION, which when applied to a value x, returns a value
    return functionPoly

    
    
L = ([1, 2, 3, 4])#(10)
x = 10

print(general_poly(L))