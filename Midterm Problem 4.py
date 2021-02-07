# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:23:01 2019

@author: Matt
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    N = [] # create an empty list
    L.reverse() # reverse the elemnts in L
    
    for element in range(len(L)):
        Q = L[element] # create a dummy list that only has a single element of L
        Q.reverse() # reverses that single element of L
        N.append(Q) # add that reversed element of L to N

    return N ## N should L reversed, and every list element of L reversed

#L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
#deep_reverse(L) 
#print(L)    
L = [[1, 2], [3, 4], [5, 6, 7]]
# function returns [[7, 6, 5], [4, 3], [2,1]]
print(deep_reverse(L[:]))