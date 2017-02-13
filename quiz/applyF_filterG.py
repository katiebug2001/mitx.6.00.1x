#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:06:25 2017

@author: katiebug
"""
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    l = L[:]
    for i in l:
        if g(f(i)):
            pass
        else:
            L.remove(i)
    
    if L == []:
        return -1
    else:  
        return max(L)

            
def f(i):
    return i - 10
def g(i):
    return i < 0

L = []
print(applyF_filterG(L, f, g))
print(L)
