# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:24:16 2019

@author: Matt
"""

## This program will print the longest substring of s in which the letters occur in alphabetical order 

s = 'azcbobobegghakl' #answer is beggh

n = 0 # iterative index number of input string s
l = len(s) # length of input string
substringCount = 0 # dummy variable to keep track of current longest substring in alphabetical order, int
substringMax = 0 # longest substring in alphabetical order, int
substring = 'fart' # dummy variable to keep track of current longest substring, string
substringPrint = s[n] # longest substring in aplphabetical order to print, string


for n in range(l):

    if substring == 'fart': #this is to initialise the count, and avoid errors with s[n-1] being larger than s[n]
        substringCount = substringCount + 1
        substring = s[n]
        n = n + 1
        
    elif s[n] >= s[n-1] and substringCount >= substringMax: # this elif will keep track of the first longest substring to print
        substringCount = substringCount + 1
        substringMax = substringCount
        substring = substring + s[n]
        substringPrint = substring # these should all be strings
        n = n + 1

    elif  s[n] >= s[n-1]: # and substringCount >= substringMax:
        substringCount = substringCount + 1
        substring = substring + s[n]
        n = n + 1 
    
    else: 
        substringCount = 1
        substring = s[n]        
        n = n + 1
        
print('Longest substring in alphabetical order is:',substringPrint)