# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:24:16 2019

@author: Matt
"""

## This program will print the longest substring of s in which the letters occur in alphabetical order 

s = 'azcbobobegghaklmn' #answer is beggh

n = 0 # iterative index number of input string s
l = len(s) # length of input string
substringCount = 0 # dummy variable to keep track of current longest substring in alphabetical order, int
substringMax = 0 # longest substring in alphabetical order, int
substring = s[n] # dummy variable to keep track of current longest substring, string
substringPrint = s[n] # longest substring in aplphabetical order to print, string

f = '30'


for n in range(l):

    if s[n] < f: #this is to initialise the count, and avoid errors with s[n-1] being larger than s[n]
        f = -100
        substringCount = substringCount + 1
        n = n + 1
        
    elif s[n] >= s[n-1] and substringCount >= substringMax: # this elif will keep track of the first longest substring to print
        substringCount = substringCount + 1
        substringMax = substringCount
        substring = substring + s[n]
        substringPrint = substring #+ s[n] # these should all be strings
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

#what if I assigned numerical value to each letter of the alphabet
#then had to find and keep the string with the longest "train" of increasing
#integer values i.e. a =1. b =2, c = 3, etc...
#therefore, stop counting if a > n, b > n, c > , etc
#where n = the previous value in the string

# abcda would be 12341, where n1 = 1, n2 = 2, n3 = 3, n4 = 4, n5 = 1
# n5 < n4, so stop the loop and somehow keep the last substring saved
# substring would be = 'n1' + 'n2' + 'n3' + 'n4', saved as a string