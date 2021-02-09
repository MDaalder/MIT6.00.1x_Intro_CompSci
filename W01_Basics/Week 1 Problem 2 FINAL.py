# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:24:16 2019

@author: Matt
"""

## This program will count the number of 'bob' within a string of characters 


var = 'bob' # Assign bob to a variable

# Ask user to input a string of characters to be evaluated 

# s = 'azcbobobebobgghaklbobobboboboob'

l = len(s) # length of input string
bobs = 0 # number of vowels in input string s
n = 0 # iterative index number of input string s

for n in range(l-2):

    if s[0+n:n+3] in var:
        bobs = bobs + 1
        n = n + 1
        
    else: 
        bobs = bobs
        n = n + 1
        
print('Number of times bob occurs is:',bobs)