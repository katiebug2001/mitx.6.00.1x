#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:45:40 2017

@author: katiebug
"""

def f(x,y):
    return x + y

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    intersectDict = {}
    unionDict = {}

    for key in d1:
        if key in d2:
            thisValue = f(d1[key], d2[key])
            intersectDict[key] = thisValue
        else:
            unionDict[key] = d1[key]

    for key in d2:
        if key not in intersectDict:
            unionDict[key] = d2[key]

    theTuple = (intersectDict, unionDict)
    #print(theTuple)
    return theTuple
    
d1 = {1:30, 2:12}
d2 = {1:52}
dict_interdiff(d1, d2)

