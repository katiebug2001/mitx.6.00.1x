#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:35:18 2017

@author: katiebug
"""
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    for list in L:
        list.reverse()
        #print(list)
    #print(L)
    
    L.reverse()
    #print(L)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)

print(L)