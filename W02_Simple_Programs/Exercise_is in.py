# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:02:44 2019

@author: Matt
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) < 1:
        return False
    
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    if char == aStr[int(len(aStr)/2)]:
        return True
    
    elif char < aStr[int(len(aStr)/2)]:
        aStr = aStr[0:int(len(aStr)/2)]
        return isIn(char, aStr)
    
    else:
        aStr = aStr[int(len(aStr)/2):len(aStr)]
        return isIn(char, aStr)