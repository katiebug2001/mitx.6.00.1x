#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:38:34 2017

@author: katiebug
"""
#code with bug
#def integerDivision(x, a):
#    """
#    x: a non-negative integer argument
#   a: a positive integer argument
#
#    returns: integer, the integer division of x divided by a.
#    """
#    while x >= a:
#        count += 1
#        x = x - a
#    return count


#code debugged

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(6,2))