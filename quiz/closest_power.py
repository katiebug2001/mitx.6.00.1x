#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:38:41 2017

@author: katiebug
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    last_exp = 0
    this_exp = 1
    
    
    while abs(num - (base ** last_exp)) > abs(num - (base ** this_exp)):
        last_exp, this_exp = this_exp, this_exp + 1
        
    return last_exp
    
print(closest_power(3, 12))
print(closest_power(4, 12))
print(closest_power(4, 1))