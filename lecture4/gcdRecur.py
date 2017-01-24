#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:31:16 2017

@author: katiebug
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0 :
        gcd = a
    else :
        gcd = (gcdRecur(b, a % b))
    return gcd

    
print(gcdRecur(3, 6))
print(gcdRecur(32, 72))
print(gcdRecur(437, 437))
print(gcdRecur(33, 4))
print(gcdRecur(100, 50))