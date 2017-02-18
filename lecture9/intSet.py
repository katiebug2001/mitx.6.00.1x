#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:24:56 2017

@author: katiebug
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, another_intSet):
        the_intersect = intSet()
        for int in self:
            if another_intSet.member(int):
                the_intersect.insert(int)
        return the_intersect
    
    def __len__(self):
        return len(self.vals)
        
    def __iter__(self):
        return self.vals.__iter__()

test_intset = intSet()
test_intset.vals.extend([9, 10, 11])
other_intset = intSet()
other_intset.vals.extend([7, 8, 9])

print(test_intset.intersect(other_intset))
print(len(test_intset))

try:
    for int in test_intset:
        print(str(int))
except:
    print("it didn't work.")
    