# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:59:49 2019

@author: Matt
"""

# this program converts an integer number into a binary
# if binary 101 = 1*2**2 + 0*2**1 + 1*2**0 = 5

# then, if we take the remainder relative to 2 (x%2) of this number
# that gives us the last binary bit

# if we then divide 5 by 2 (5//2) all the bits get shifted right
# 5//2 = 1*2**1 + 0*2**0 = 10

# keep doing successive divisions; now remainder gets next bit, and so on

# we've converted to binary.

inNum = int(input('Enter an integer to convert to binary: '))

num = inNum

if num < 0:
    isNeg = True
    num = abs(num)
    
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'
    
while num > 0:
    result = str(num%2) + result
    num = num//2
    
if isNeg:
    result = '-' + result    
        
print('The binary of your integer ' + str(inNum) + ' is ' + str(result))
