# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:53:07 2019

@author: Matt

creating a more efficient computation of fibonacci sequence using a dictionary
computes and stores each fibonacci sequence number to be called when needed, instead
of computing each value over and over again.


"""

# Original, inefficient code

def fib(n):
    global numFibCalls #global means object is accessible outside of scope of function
    numFibCalls += 1 # counts how many times the function fib is called
    
    if n == 1: # base case, known answer
        return 1
    
    elif n == 2: # base case, known answer
        return 2
    
    else:
        return fib(n-1) + fib(n-2)
    
# New, efficient code that uses a dictionary
        
def fibEfficient(n, d):
    global numFibCalls
    numFibCalls += 1
    
    if n in d: # if n is already in dictionary d, then return that value
        return d[n]
    
    else:
        ans = fibEfficient(n-1, d) + fibEfficient(n-2, d) # compute answer for nth fibonacci number
        d[n] = ans # create new dictionary entry
        return ans # return that answer

numFibCalls = 0
nth = 20 # which fibonacci number to compute
d = {1:1, 2:2} # base cases, already know the the answers to n=1 and n=2

print('Computing Fibonacci number', nth)
print(' ')
print('Answer:', fib(nth))
print('# of function calls = ', numFibCalls)
print(' ')

numFibCalls = 0

print('Answer:', fibEfficient(nth, d))
print('# of function calls = ', numFibCalls)
    