# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:10:21 2019

@author: Matt
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']} # this is a dictionary titled animals

animals['d'] = ['donkey'] # adding key 'd' and value 'donkey'
#animals['d'].append('dog') # appending values 'dog' and 'dingo' to key 'd'
#animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # thought process:
    # find which key has the greatest length (max value)
    # somehow remember this key
    # then access and return this key
    
    dummyDict = {}
    dummyList = []    
    
    for word in aDict: # iterates through keys in the dictionary aDict
        
        dummyDict[word] = len(aDict[word]) # creates a dictionary with str:int, where int is the number of entires associated with each str
    
    entries = dummyDict.values() # number of entries assigned to each key
    largest = max(entries) # largest number of entries assigned to a key
        
    for i in dummyDict:
        if dummyDict[i] == largest: # if the value assigned to key [i] is the same as the largest, then add it to a list for tracking
            dummyList.append(i)
    
    #result = dummyDict.keys()
    result = dummyList
    result = ''.join(dummyList) # changes the dummyList into string chars to return
    #result = result.split()
    return (result) # returns the key(s) in the dictionary associated with the largest number of values


print((biggest(animals))) # prints the sum of number of values in the dictionary


"""
another method
"""

def biggestAlt(aDictAlt):
    
    maxLen = 0
    key = []
    
    for (k, v) in aDictAlt.items():
        if len(v) >= maxLen:
            maxLen = len(v)
            key.append(k)
            
    return (key)

print(biggestAlt(animals))