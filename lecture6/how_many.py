#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:31:18 2017

@author: katiebug
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values = aDict.values()
    #print(values)
    list(values)
    #print(values)
    num_values = 0
    
    for lists in values:
        if len(lists) >= 1:
            for things in lists:
                num_values += 1
    return num_values
    
#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')"""

#print(animals)

#print(how_many(animals))
