# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:49:41 2019

@author: Matt
"""
# L is sorted in increasing order, positive integers

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    


def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)): # new line
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [4, 7, 1, 10, 2, 6]

print(swapSort(L), 'Final')

L = [4, 7, 1, 10, 2, 6]
print(modSwapSort(L), 'Final new')