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
    listToBeAdded = []
    for myIndex in range(len(listA)):
        myProduct = listA[myIndex] * listB[myIndex]
        listToBeAdded.append(myProduct)
        #print('listToBeAdded is: {}'.format(listToBeAdded))
    #print('listToBeAdded is finished; the list to be added is {}'.format(listToBeAdded))
    
    finalSum = 0
    for theNumber in listToBeAdded:
        #print('finalSum is not finished; the sum is {}'.format(finalSum))
        finalSum += theNumber
    #print('finalSum is finished; the final sum is {}'.format(finalSum))
    return finalSum
    
print(dotProduct([1, 2, 3], [4, 5, 6]))