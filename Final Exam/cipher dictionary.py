# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:01:03 2019

@author: Matt
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    cipherDict = {}
    decoded = []
    x = 0
    
    for letter in map_from:
        cipherDict[letter] = map_to[x]
        x += 1
      
    for letter in code:
        decoded.append(cipherDict[letter])
    
    answer = ''.join(decoded)
    
    
    return(cipherDict, answer)

print(cipher("abcd", "dcba", "dab"))