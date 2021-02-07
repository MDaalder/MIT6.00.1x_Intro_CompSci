# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:19:19 2019

@author: Matt

An example of classes and hierarchies.
Has superclass Animal, subclasses Cat, Rabbit, Person
Has a subclass of subclass Person, called Student.

Examples of getter & setter methods, class variables and inherited methods.
"""
import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
    """Define getters to get data attributes outside of the class"""    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    
    """Define setters to set data attributes outside of the class"""
    def set_age(self, newage):
        self.age = newage
    # the default name if no value given in a blank string    
    def set_name(self, newname=""):
        self.name = newname
    
    """What to print when print(Animal()) called.
        Overrides Animal (parent) string method."""
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)
  
    
    
"""New subclass Cat, of parent class Animal.
Do not need to use __init__, because it inherits data and behaviours
from the parent class. Subclass Cat will inherit all methods/data/behaviours 
from class Animal unless otherwise changed."""    
class Cat(Animal):
    def speak(self):
        print("meow")   
    # this string method will replace the previous Animal for all subclass of Cat
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)



"""New subclass Rabbit, or parent class Animal.
Uses a class variable 'tag' to create unique id's for each new rabbit instance.
"""
    
class Rabbit(Animal):
    tag = 1 # class variable outside of __init__
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.ta += 1 # incrementing class variable changes it for all instances that may reference it
    
    """Getter methods. get_rid/_parent1/_parent2 are specific to Rabbit class.
    get_name/_age are inherited from Animal."""
    def get_rid(self):
        return str(self.rid).zfill(3) #zfill(3) pads the string with zeros, prints 001 instead of 1
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)
    
    
    def __add__(self, other):
        #returns object of same type as this class
        return Rabbit(0, self, other) # 0 = age, self = parent1, other = parent2

    """Special method to compare two instances of Rabbit class.
    Decide that two rabbits are equal if they have the same two parents.
    Compare ids of parents (rid) since ids are unique (due to class variable 'tag')
    We have set up booleans, and will return the result True if the rabbits have the same two parents."""
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                    and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                    and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
        
    
class Person(Animal): # parent class is Animal
    def __init__(self, name, age):  
        Animal.__init__(self, age) # call Animal __init__ instance 
        Animal.set_name(self, name) # call Animal's method to set name (class.method())
        self.friends = [] # add a new data attribute
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self): # overrie Animal string method
        return "person"+str(self.name)+":"+str(self.age)



""" Create a new subclass Student that inherits Person and Animal attributes."""
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self= major
    def speak(self):
        r = random.random() # random gives a float in [0,1]
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self): # overries Person string method
        return "student"+str(self.name)+":"+str(self.age)+":"+str(self.major)