#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:04:45 2017

@author: katiebug
"""

def addVectors(v1, v2):
    """assumes v1 and v2 are lists of ints. returns a list containing the pointwise sum of the elements in v1 and v2"""
    while len(v1) != len(v2):
        if len(v1) < len(v2):
            v1.append(0)
        else:
            v2.append(0)
    if len(v1) == 0:
        return []
    my_pointwise = []
    for my_index in range(len(v1)):
        my_sum = v1[my_index] + v2[my_index]
        my_pointwise.append(my_sum)
    return my_pointwise
    
print(addVectors([9, 8, 7, 10], [1, 2, 3]))