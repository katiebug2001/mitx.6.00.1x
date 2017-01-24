#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:03:39 2017

@author: katiebug
"""

s = 'azcbobobegghakl'

cur_str = s[0]

big_str = ''

for index in range(len(s) - 1) :
    if s[index] <= s[index + 1] :
        cur_str = cur_str + s[index + 1]
    else :
        if len(cur_str) > len(big_str):
            big_str = cur_str
        cur_str = s[index + 1]

if len(cur_str) > len(big_str):
    big_str = cur_str

print('Longest substring in alphabetical order is: ' + big_str)