# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:11:26 2019

@author: md131
"""

class intSet(object):
    """ An intSet is a set of integers.
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    
    def __init__(self): # creates instances, no argument other than self because it starts as empty
        """Create an empty set of integers """
        self.vals = []
        
    def insert(self, e): # insert things into the set. Enforce the representational invariant.
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals: # When I want to insert an element into an instance of IntegerSet, checks, is that element inside the list? 
            self.vals.append(e) 
            
    def member(self, e): # check if e is in the list, using the property that list is an iterable
        """Assumes e is an integer.
        Returns True if e is in self, and False otherwise"""
        return e in self.vals
    
    def remove(self, e): # uses property of exceptions to remove something from a list. It will only remove the first instance of element e
        """Assumes e is an integer and removes e from self.
        Raises ValueError if e is not in self"""
        try: 
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def __str__(self): # define string to determine how I want to print the elements of a list
        """Returns a string representation of self"""
        self.vals.sort()
        result = '' # empty string
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' # returns everything except the trailing comma
    

s = intSet()
print(s) # should be {}

s.insert(3)
s.insert(4)
s.insert(3)
s.insert(2)

print(s) # should be {2, 3, 4}, sorts and removes the extra 3

print(s.member(3)) # should return True
print(s.member(6)) # should return False

s.remove(3)
s.insert(6)

print(s) # {2, 4, 6}

#s.remove(3) # will return "ValueError: 3 not found"