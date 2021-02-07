# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:59:07 2019

@author: Matt
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    
    i.e. [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened to [1,'a','cat',2,3,'dog',4,5] (order matters)
    '''
    
# recursion will be useful
# need to flatten every element of the original list
# to check if an element can be flattened, the element must be object type list

## will need to check if the element is a list, if not, convert it to one
    
    #global newList
    newList = []
    #print('Input list', aList)
    
    for i in range(len(aList)):
        
            
        if type(aList[i]) == tuple:
            list(aList[i])
            newList = newList + flatten(aList[i])
                    
        elif type(aList[i]) == list:
            #print('Sublist to be flattened', aList[i])
            #print('New list', newList)
            newList = newList + flatten(aList[i])
         
        else: #if type(aList[i]) != list:
            #print('Index aList', i, '=', aList[i])
            newList.append(aList[i])
            #print('New list', newList)
            
    return newList
 
#aList = [1,'a',['cat'],2]   
aList = [[1,'a',['cat'],2],[[[3]],'dog'],[(1, 'one', 7)],4,5]
print('Input list', aList)
print('The flattened test result', flatten(aList))
        