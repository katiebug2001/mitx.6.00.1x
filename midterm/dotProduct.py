#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:04:06 2017

@author: katiebug
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    returns the sum of the pairwise products of listA and listB
    '''
    finalSum = 0

    for myIndex in range(len(listA)):
        myProduct = listA[myIndex] * listB[myIndex]
        finalSum += myProduct
        #print('listToBeAdded is: {}'.format(listToBeAdded))
    #print('listToBeAdded is finished; the list to be added is {}'.format(listToBeAdded))
    
    return finalSum
    
print(dotProduct([1, 2, 3], [4, 5, 6]))