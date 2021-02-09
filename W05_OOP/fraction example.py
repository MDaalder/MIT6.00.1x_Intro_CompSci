# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:53:13 2019

@author: md131
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                    + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                    - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self): # convert fractions into floats
        return self.getNumer() / self.getDenom()
        
        
        
oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)
threeQuarters = fraction(3, 4)

print(oneHalf.getNumer()) # this is a procedure, so need to invoke it with ()

new = oneHalf + twoThirds
print(new)

secondNew = twoThirds - threeQuarters
print(secondNew)

print(secondNew.convert())

print(fraction.convert(secondNew))  