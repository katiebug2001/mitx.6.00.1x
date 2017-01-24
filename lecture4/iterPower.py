#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:28:38 2017

@author: katiebug
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = 1
    
    while exp != 0:
        ans = (ans * base)
        exp -= 1
    
    return ans
    
   
print(iterPower(2, 4))