#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:56:58 2017

@author: katiebug
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #print( 'string: ' + aStr + ' length: ' + str(len(aStr)) + ' index: ' + str(int(len(aStr)/2)) )
    
    if(len(aStr) == 0) :
        return False
    else :
        index = int(len(aStr)/2)
        check_char = aStr[index]
                  
        if char == check_char :
            return True
        else :
            if check_char > char:
                return isIn(char, aStr[ : index])
            else :
                return isIn(char, aStr[(index + 1)  : ])

print(isIn('c','abcde'))
print(isIn('d','abcde'))
print(isIn('b','abcde'))
print(isIn('z','abcde'))
print(isIn('z','abcdef'))
print(isIn('z','k'))