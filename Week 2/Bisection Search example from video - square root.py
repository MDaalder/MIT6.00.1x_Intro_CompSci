# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 01:53:55 2019

@author: Matt
"""

x = 100 # number we are trying to find the square root of. Does not need to be an integer
epsilon = 0.001 # acceptable "error", make it smaller for more accurate answer, but longer compute time
numGuesses = 0
low = 0.0
high = x
guess = (high + low)/2.0 #this is a guess at the square root answer, between 0 and x

while abs(guess**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
    numGuesses += 1
    if guess**2 < x:
        low = guess # the guess^2 is smaller than x, therefore the real answer must be smaller than the guess
    else:
        high = guess # the guess^2 is largerer than x, therefore the real answer must be larger than the guess
    guess = (high + low)/2.0

ans = guess    
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))