#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:42:00 2017

@author: katiebug
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    if exp == 0:
        ans = 1
    else:
        ans = base * recurPower(base, (exp - 1))
    
    return ans

print(recurPower(2, 0))
print(recurPower(2, 1))
print(recurPower(2, 2))
print(recurPower(2, 3))
print(recurPower(2.5, 2))
