#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:33:04 2017

@author: katiebug
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    def flatten_the_other_list(aList):
        
        for element in aList:
            #print('the new list is {}'.format(aNewList))
            if type(element) == list:
                #print('flattening the element{}'.format(element))
                flatten_the_other_list(element)
            else: 
                aNewList.append(element)
        return aNewList

    aNewList = []

    for element in aList:
        #print('the new list is {}'.format(aNewList))
        if type(element) == list:
            #print('flattening the element{}'.format(element))
            aNewList.extend(flatten(element))
        else: 
            aNewList.append(element)
    return aNewList
    
print(flatten(['k',['a',['t',['i',['e']]]]]))