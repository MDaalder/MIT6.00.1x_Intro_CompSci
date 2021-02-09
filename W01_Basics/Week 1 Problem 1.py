# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:24:16 2019

@author: Matt
"""

## This program will count the number of vowels within a string of characters 

# Assign the vowels to be counted to variables
a = 'a'
e = 'e'
E = 'E'
i = 'i'
o = 'o'
u = 'u'

allvowels = 'AaEeIiOoUu'
#s = 'azcbobobegghakl'

# Ask user to input a string of characters to be evaluated
x = input('Enter a string of characters here to count the number of vowels contained within: ')
s = x # assign the input string to variable s

l = len(s) # length of input string
vowels = 0 # number of vowels in input string s
n = 0 # iterative index number of input string s

for n in range(l-1):

    if s[n] in allvowels:
        vowels = vowels + 1
        n = n + 1
#while n <= l-1:
    
#    if s[n] == a:
#        vowels = vowels + 1
#        n = n + 1
#        
#    elif s[n] == e:
#        vowels = vowels + 1
#        n = n + 1
#    
#    elif s[n] == i:
#        vowels = vowels + 1
#        n = n + 1    
#
#    elif s[n] == o:
#        vowels = vowels + 1
#        n = n + 1        
#
#    elif s[n] == u:
#        vowels = vowels + 1
#        n = n + 1
        
    else: 
        vowels = vowels
        n = n + 1
        

print('Number of vowels:',vowels)