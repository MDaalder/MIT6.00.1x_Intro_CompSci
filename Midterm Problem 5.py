# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:38:25 2019

@author: Matt
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    
    This function takes in a a dictionary, and returns a list
    
    Keys in aDict map to integer values that are unique (values appear only once in aDict)
    
    List of keys returned should be in increasing order.
    If there are no unique values in aDict, the function should return an empy list
.    '''
    dummyList = []
    dummyDict = {}
    
    result = []
    
    intValues = aDict.values() # gets values of dictionary
#    keyValues = aDict.keys() # gets keys of dictionary
#    print('Values in aDict', intValues)
#    print('Keys in aDict', keyValues)
    
    for t in intValues: # this will iterate through values of dictionary, and create key entries of int value k to keep a count of how many times that int comes up
        if t in dummyDict: # if the value is already in the dictionary, add 1 to entry count
            dummyDict[t] += 1
        if t not in dummyDict: # if the value is not already in dict, create an entry
            dummyDict[t] = 1
    
    
    for k in dummyDict: # itereates through all int keys in the new dictionary (which are values in original dictionary)
        if dummyDict[k] == 1: # if the value of that key is 1, that int is unique in the dictionary
            dummyList.append(k) # add that int value to the list of unique dictionary values
    
    for w in aDict: # iterates through keys in aDict
        if aDict[w] in dummyList: # if the value of aDict[key] is in the dummyList of unique dictionary values
            result.append(w) # record that aDict key to a list to be sorted and printed
        
    result.sort()
           
    return result    
        
#aDict = {'a':1, 'b': 2, 'c': 4, 'd': 0, 'e': 3, 'f': 2}
# answer [0, 1, 3, 4]
#aDict = {1:1, 2: 2, 8: 4, 0: 0, 5: 3, 3: 2}
# answer [4, 5, 8]
aDict = {2: 0, 3: 3, 6: 1}
#answer [2, 3, 6]
print(uniqueValues(aDict))
