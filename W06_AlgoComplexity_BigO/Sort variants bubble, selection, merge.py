# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:21:21 2019

@author: md131

Comparison of sorting methods and their complexities in Big Oh notation.
"""


""" Bubble sort compares consecutive pairs of elements. Overall complexity is O(n^2) where n is len(L)
Swaps elements in the pair such that smaller is first.
When reach the end of the list, start the sort again.
Stop when no more sorts have to be made. """

def bubbleSort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]: # if L[j-1] is larger than L[j], put element L[j] to the left of L[j-1] by swapping their index values
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


""" Selection sort. Overall complexity is O(n^2) where n is len(L)
1st step: extract the minimum element from the suffix, swap it with index 0 [0] and put into the prefix.
2nd step: extract the minimum element from the remainin sublist (suffix), swap it with index 1 [1], becomes the last element of the prefix.

prefix: L[0:i]
suffix: L[i+1, len(L)]
Always iterating up i. Prefix is always sorted, where no element is larger than in the suffix. """

def selectionSort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt] # L[suffixSt] is larger than L[i], swap the two. Put the lower value on the left of the list
            suffixSt += 1



""" Merge Sort: overall complexity is O(n log n) where n is len(L)
    Successively divide a large list into two halves until you have lists of length < 2. These are considered sorted.
    Then compare the smallest value of two lists one at a time, and add the smallest value to the end of a new sublist. This is the merging part.
    If a sublist is empty while comparing, add the remaining values from the other sublist to the result.
    Then merge your new, but longer, sublists in the same way as above.
    Repeat until you have a final sorted list. This essentially contains all of the merged, sorted sublists."""

# complexity O(log n), n is len(L)
def mergeSort(L):
    if len(L) < 2: # base case, list of length < 2 is considered sorted
        return L[:]
    else:
        middle = len(L)//2 # integer divide by two
        left = mergeSort(L[:middle]) # divide the list and mergeSort again, until len(L) < 2
        right = mergeSort(L[middle:]) # divide the list "
        return merge(left, right) # requires the next function 'merge, conquer with the merge step

# complexity O(n), n is len(L)
def merge(left, right):
    result = []
    i, j = 0,0
    while i < len(left) and j < len(right): # assumes right and left sublists are already ordered
        if left[i] < right[i]:
            result.append(left[i])
            i += 1 # move indices for sublists depending on which sublist holds the next smallest element 
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)): # when the right sublist is empty, append the left one to it
        result.append(left[i])
        i += 1
    while (j < len(right[j])):
        result.append(right[j]) # when the left sublist is empty, append the right one to it
        j += 1
    return result