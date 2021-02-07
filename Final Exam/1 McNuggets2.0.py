# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:33:52 2019

@author: Matt
"""

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    # solving for n - 6a - 9b - 20c = 0
    if n == 0:
        return True
    
    for a in range(n):
        if n-(6*a) == 0:
            return True
        
        for b in range(n):
            if n-(9*b) == 0:
                return True
            if n-(6*a + 9*b) == 0:
                return True
            
            for c in range(n):
                if n-(20*c) == 0:
                    return True
                if n - 6*a - 9*b - 20*c == 0:
                    return True
                
    return False
    

# test case
x = 0
print(McNuggets(x))