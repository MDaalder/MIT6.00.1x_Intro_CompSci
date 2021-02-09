# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 02:10:24 2019

@author: Matt
"""

print('Please think of a number between 0 and 100!')

low = 0
high = 100
guess = (high - low)//2

while guess >= 0 and guess < 100:
    
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + '?')
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate' I guessed correctly. ")

    if user == 'h':
       high = guess # Guess was too high. So make the current guess the highest possible guess.
              
    elif user == 'l':
       low = guess # Guess was too low. So make the current guess the lowest possible guess.   
              
    elif user == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    
    else:
        print('Sorry, I did not understand your input.')
    
    
