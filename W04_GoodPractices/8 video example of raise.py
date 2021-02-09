# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:37:50 2019

@author: Matt
"""

def get_ratios(L1, L2):
    """ assumes L1 and L2 are lists of equal length of numbers
    returns a list containing L1[i]/L2[i]"""
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN = not a number
        except:
            raise ValueError('get_ratios called with bad arg')
            
    return ratios



L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
#L2 = [5, 6, 7, 0] #test case for div 0
#L2 = [5, 6, 7] # test case for bad argument len L1 != len L2
