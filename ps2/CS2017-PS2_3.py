#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:31:41 2017

@author: katiebug
"""
balance = 999999
annualInterestRate = 0.18


def balance_left(balance, annualInterestRate, payment):
    year = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    for month in year:
        #print( 'in ' + month + ' balance is equal to ' + str(balance))
        this_month = round( (balance - payment) + ((annualInterestRate / 12) * (balance - payment)), 2)
        balance = this_month
    #print(str(balance))
    return balance

#upper bound is 1/12 of the balance after having its interest compounded for the entire year
upper_bound = (balance * (1 + annualInterestRate/12) ** 12) / 12.0
lower_bound = balance/12
payment = (lower_bound + upper_bound)/2

while True:
    end_of_year_balance = balance_left(balance, annualInterestRate, payment) 
    
    if ((upper_bound - lower_bound) < .02):
        print('Lowest Payment: {:.2f}'.format(payment))
        break
    
    elif end_of_year_balance > 0:
        lower_bound = payment
        payment = round(((lower_bound + upper_bound) / 2), 2)
        #print('payment was too small; lower bound is now {} and payment is now {}. The upper bound is {} '.format(lower_bound, payment, upper_bound))
        
    else:
        upper_bound = payment
        payment = round(((lower_bound + upper_bound) / 2), 2)
        #print('payment was too big; upper bound is now {} and payment is now {}. The lower bound is {}'.format(upper_bound, payment, lower_bound))

        

