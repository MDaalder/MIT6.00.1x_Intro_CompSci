# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:26:13 2019

@author: Matt
"""

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

# this avg can't handle division by 0
#def avg(grades):
#    return sum(grades)/len(grades)


test_grades = [[['pete', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
                [['deadpool'], []]]

# this avg will handle the division by 0
# but it will enter a value of 'None' for the average grade
#def avg(grades):
#    try:
#        return sum(grades)/len(grades)
#    except ZeroDivisionError:
#        print('no grades data')
        
# this avg will handle the division by 0
# and it will enter a value of 0.0 for the average grade        
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0