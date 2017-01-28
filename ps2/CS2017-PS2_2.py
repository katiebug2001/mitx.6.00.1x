#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:55:48 2017

@author: katiebug
"""
balance = 3926
annualInterestRate = 0.2

upper_bound = balance
# lower bound is a multiple of ten that is the lowest possible payment for every month
lower_bound =  int(round( ( (balance / 12 ) + 5 ), -1 ))

def balance_left(balance, annualInterestRate, payment):
    year = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    for month in year:
        #print( 'in ' + month + ' balance is equal to ' + str(balance))
        this_month = round( (balance - payment) + ((annualInterestRate/12) * (balance - payment)), 2)
        balance = this_month
    #print(str(balance))
    return balance

for payment in range(lower_bound, upper_bound, 10):
    if (balance_left(balance, annualInterestRate, payment)) <= 0:
        break
print('Lowest Payment: ' + str(payment))     
