# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:10:21 2019

@author: Matt
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']} # this is a dictionary titled animals

animals['d'] = ['donkey'] # adding key 'd' and value 'donkey'
animals['d'].append('dog') # appending values 'dog' and 'dingo' to key 'd'
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    critterSum = 0
    
    for word in aDict: # iterates through keys in the dictionary aDict
        
        critterSum += len(aDict[word]) # adds the number of values assigned to each key to a global counter
      
    return critterSum # returns the number of values stored in the dictionary

print(how_many(animals)) # prints the sum of number of values in the dictionary
