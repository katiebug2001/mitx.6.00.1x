#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:45:15 2017

@author: katiebug
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    iters = 1
    my_tup = ()
    for x in (aTup):
       
        if iters % 2 != 0 :
            my_tup = (my_tup + (x,))
        
        iters += 1
        
    return my_tup
        
            
print(oddTuples( ( 'katie', 'hello', 'is', 'not', 'awesome' ) ) )