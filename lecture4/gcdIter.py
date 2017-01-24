#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:54:15 2017

@author: katiebug
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a > b :
        gcd = b
        big = a
        small = b
    else :
        gcd = a
        big = b
        small = a
        
    while gcd >= 1:
        if (big % gcd) == 0 and (small % gcd) == 0 :    
                return gcd
        else :
            gcd -= 1
        
print(gcdIter(304, 171))
print(gcdIter(180, 75))
print(gcdIter(42, 27))
print(gcdIter(437, 437))
print(gcdIter(34, 5))
