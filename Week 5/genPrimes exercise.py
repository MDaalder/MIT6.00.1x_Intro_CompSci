# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:46:42 2019

@author: Matt
"""

#def genFib():
#    fibn_1 = 1
#    fibn_2 = 0
#    while True:
#        next = fibn_1 + fibn_2
#        yield next
#        fibn_2 = fibn_1
#        fibn_1 = next
        

def genPrimes():
    x = 1
    prime = []
    xval = None
    
    while True:
        x += 1
        xval = True
        
        for p in prime:
            if (x % p) == 0:
                xval = False
                
        if xval == True:
            prime.append(x)
            next = x
            yield next
        
            
foo = genPrimes()
#foo.__next__()