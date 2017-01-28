#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:39:48 2017

@author: katiebug
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

year = [ 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec' ]
for month in year :
    minimum_payment = ( balance * monthlyPaymentRate )
    #new balance is balance before monthly interest
    new_balance = (balance - minimum_payment)
    balance = ( new_balance + ( (annualInterestRate/12) * new_balance ) )
    balance = round(balance, 2)
    
print('Remaining balance: ' + str(balance))
    