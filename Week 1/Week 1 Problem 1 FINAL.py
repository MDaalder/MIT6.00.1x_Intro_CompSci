# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:24:16 2019

@author: Matt
"""

## This program will count the number of vowels within a string of characters 


allvowels = 'AaEeIiOoUu' # Assign all vowels to a variable

# Ask user to input a string of characters to be evaluated 
s = input('Enter a string of characters here to count the number of vowels contained within: ')

# s = 'azcbobobegghakl'

l = len(s) # length of input string
vowels = 0 # number of vowels in input string s
n = 0 # iterative index number of input string s

for n in range(l):

    if s[n] in allvowels:
        vowels = vowels + 1
        n = n + 1
        
    else: 
        vowels = vowels
        n = n + 1
        
print('Number of vowels:',vowels)