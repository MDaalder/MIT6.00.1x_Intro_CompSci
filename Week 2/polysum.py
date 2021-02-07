
"""

@author: Matt

Function calculates the sum of the area and perimeter^2 of a regular polygon to 4 decimal points
A regular polygon has n sides, each with length s

n number of sides
s length of each side

"""

def polysum(n, s):
    
    import math    
    
    area = (0.25*n*s**2)/(math.tan(math.pi/n)) # area of the polygon
    perim = s*n # perimeter of the polygon
    
    return round((float(area + perim**2)), 4) # returns the answer, to 4 decimal points