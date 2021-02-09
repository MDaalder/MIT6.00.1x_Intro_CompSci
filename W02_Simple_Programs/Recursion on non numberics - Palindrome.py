# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:49:25 2019

@author: Matt
"""

def isPalindrome(s):
    
    def toChars(s): #converts strings to characters, removes all punctuation, spaces and uppercase
        s = s.lower()
        ans = ''
        for c in s: # iteration of string
            if c in 'abcdefghijklmnopqrstuvwxyz': # populating the alphabet into c to check the string for all characters
                ans = ans + c # check if it's a character, if so add it in
        return ans
    
    def isPal(s):
        if len(s) <= 1: # base case, if len(s) is 1 or less characters, then it's a palindrome
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
            #check to see if first and last chars are the same, then return everything in the middle and run again
        
    return isPal(toChars(s))

print('')
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a Palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))