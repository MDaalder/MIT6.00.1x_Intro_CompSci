# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:07:13 2019

@author: md131

aTup: a tuple

returns: tuples, every other element of aTup
"""

def oddTuples(aTup):
    words = ()
    
    for i in range(len(aTup)):    
        
        if i%2 == 0:
            words = words + (aTup[i],)
        else:
            words = words
            
    return words

test = ('I', 'am', 'a', 'test', 'tuple')

print('Odd tuples:', oddTuples(test))

#alternative answer

def oddTuples2(aTup):
    words = ()
    index = 0
    
    while index < len(aTup):
        words += (aTup[index],)
        index += 2
    
    return words

oddTuples2(test)

print('Odd tuples 2:', oddTuples2(test))

# another alternative

def oddTuples3(aTup):
    
    # Use tuple slicing by 2 to achieve the result
    return aTup[::2]

oddTuples3(test)
print('Odd tuples 3:', oddTuples3(test))