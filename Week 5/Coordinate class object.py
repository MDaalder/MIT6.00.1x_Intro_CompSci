# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:33:04 2019

@author: Matt
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other): # first argument is self to refer to any instance, other is another parameter to method
        x_diff_sq = (self.x - other.x)**2 # dot notation to access data
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __add__(self, other): # without this line, we wouldn't be able to add Coordinate types
        return Coordinate(self.x + other.x, self.y + other.y)
    def print_time(self, x):
        print(x)
        


c = Coordinate(3, 4) # c is an instance of the class Coordinate
origin = Coordinate(0, 0) # origin is an instance of the class Coordinate