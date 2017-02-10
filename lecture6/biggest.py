#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:44:35 2017

@author: katiebug
"""

def biggest(aDict):
    keys = aDict.keys()
    length = 0
    #length = length of longest list
    key_with_most_values = ''
    
    for key in keys:
        a_list = aDict[key]
        number_strings = len(a_list)
        if number_strings >= length:
            length = number_strings
            key_with_most_values = key
        
    
    if key_with_most_values == '':
        return None
    else:
        return key_with_most_values

#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#print(biggest(animals))

pets = {'cats':['trixie', 'jupiter'], 'dogs':['red'], 'fish':['survivor', 'egsf']}
    
print(biggest(pets))










