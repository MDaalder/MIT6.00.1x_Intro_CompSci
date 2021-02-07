# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:56:34 2019

@author: md131
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return(min_nums, max_nums, unique_words)
    
(small, large, words) = get_data(((1, 'mine'),
                                 (3, 'yours'),
                                 (5, 'ours'),
                                 (7, 'mine')))

print('')
print('Smallest number in the tuple:', small)
print('Largest number in the tuple:', large)
print('Number of unique words in the tuple:', words)