# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:35:49 2019

@author: Matt
"""

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    




class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc#Location(Location.getX(tent_loc),Location.getY(tent_loc))
        self.tents = []
        self.tents.append(self.tent_loc)

        
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        
        flag = True
        
        for tent in self.tents:
            distance = Location.dist_from(tent, new_tent_loc)
            
            if distance < 0.5:
                flag = False          
       
        if flag == True:
            self.tents.append(new_tent_loc)
            return True
        
        else:
            return False
        
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        
        try:
            self.tents.remove(tent_loc)
        except:
            raise ValueError
            
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        def takeX(elem):
            return elem.getX()
        
        strTents = []
        tents = self.tents.copy()
              
        tents.sort(key=takeX)
                      
        for i in range(len(tents)):
            strTents.append(str(tents[i]))
        
        return print(strTents)
        

c = MITCampus(Location(1,2))
#print(c.getX())
#For example, if c = MITCampus(Location(1,2)) then executing the following sequence of commands:
#
c.add_tent(Location(2,3)) #should return True
#c.add_tent(Location(1,2)) #should return True
#c.add_tent(Location(0,0)) #should return False
#c.add_tent(Location(2,3)) # should return False
#c.get_tents() #should return ['<0,0>', '<1,2>', '<2,3>']