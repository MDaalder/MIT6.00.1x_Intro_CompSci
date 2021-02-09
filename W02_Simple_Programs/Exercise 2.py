# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 23:43:31 2019

@author: Matt
"""
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        print(guess, 'Gives ', abs(guess**2-x))
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))