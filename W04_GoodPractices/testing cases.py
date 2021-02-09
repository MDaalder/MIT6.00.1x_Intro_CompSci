# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:58:04 2019

@author: Matt
"""

def fancy_divide(numbers, index):
    
    try:    
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print('1')
        finally:
            print('0')
    
    except ZeroDivisionError:
        print('-2')             
            
fancy_divide([0, 2, 4], 4)


#different fancy divide function with a helper function
# will take a list and index #, and return a list of the division answers

#def fancy_divide(list_of_numbers, index):
#    denom = list_of_numbers[index]
#    return [simple_divide(item, denom) for item in list_of_numbers]
#    
#
#def simple_divide(item, denom):
#    try:
#        return item/denom
#    except ZeroDivisionError: # if zerodiverror, change result to 0
#        return 0
#
#print(fancy_divide([0, 2, 4], 0))