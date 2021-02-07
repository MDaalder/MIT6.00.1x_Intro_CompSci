# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:48:04 2019

@author: Matt
"""

""" returns a list of prime numbers between 2 and N
inclusive, sorter in increasing order"""

def primes_list(N):
    '''
    N: an integer
    '''
    primes = []
    rangeNums = []
    
    if N == 2:
        primes.append(N)
        return primes[:]
    
    for i in range(N-1):
        rangeNums.append(i+2)
    
    for num in rangeNums:
        for j in range(2,N):
            prime = True    
#            print(num, j)
            
            if num == j:
                break
            
            if num%j == 0:
                prime = False
                break
            
        if prime == True:
            primes.append(num)
        
                        
        
#    print(rangeNums[:])
#    print(primes[:])
    
    return primes[:]
        
print(primes_list(2))