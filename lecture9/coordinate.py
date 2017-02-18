#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:15:23 2017

@author: katiebug
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other_point):
        return (self.x == other_point.x) and (self.y == other_point.y)
        
    def __repr__(self):
        return 'Coordinate({}, {})'.format(self.x, self.y)
        
here = Coordinate(8, 6)
there = Coordinate(8, 6)