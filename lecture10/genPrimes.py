#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:50:33 2017

@author: katiebug
"""
import unittest

def genPrimes():
    """returns prime numbers"""
    x = 2
    primes = []
    while True:
        if is_prime(x, primes):
            primes.append(x)
            yield x
        x += 1  
        
def is_prime(n, smaller_primes):
    """determines if an integer n is prime
    smaller_primes is a list of prime numbers smaller than n"""
    for number in smaller_primes:
        if (n % number) == 0:
            return False
    return True
    
class TestGenPrimes(unittest.TestCase):
    """
    tests genPrimes()
    """
    def test_10_primes(self):
        """
        tests for 1st ten prime numbers
        """
        primeGen = genPrimes()
        ten_primes = []
        for k in range(10):
            ten_primes.append(primeGen.__next__())
        self.assertEqual([ 2,  3, 5, 7, 11, 13, 17, 19, 23, 29], ten_primes)
        
if __name__ == '__main__':
    unittest.main()

                    