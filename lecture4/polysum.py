#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:24:49 2017

@author: katiebug
"""

def polysum(n,s):
    """ n, the number of sides of a REGULAR polygon; s, the length of a side of the polygon
    polysum calculates the sum of the area and the square of the perimeter of a REGULAR polygon to four decimal places. """
    
    import math
    pi = math.pi
    
    perimeter = n * s
    squaredPerimeter = perimeter ** 2
    
    area = ( n * s**2) / (4 * math.tan(pi / n))
    
    answer = squaredPerimeter + area
    answer = round(answer, 4)
    
    return answer
    
print(polysum(4, 1.2))
    