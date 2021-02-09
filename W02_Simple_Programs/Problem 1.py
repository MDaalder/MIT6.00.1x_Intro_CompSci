# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:42:11 2019

@author: Matt

Calculates the remaining balance on a credit card after one year

Takes in initial balance, annual interest rate, minimum monthly payment rate.
"""

# this test should give answer 31.38
#balance = 42 #starting balance
#annualInterestRate = 0.2 #percentage, divide by 12 for monthly interest rate
#monthlyPaymentRate = 0.04 #percentage

def creditCard(balance, annualInterestRate, monthlyPaymentRate):

    months = 12 # number of months to calculate interest for
    monthlyInterest = annualInterestRate/12.0 #monthly interest rate
    
    for i in range(months):
        
        monthlyMin = monthlyPaymentRate * balance # minimum monthly payment
        monthlyUnpaid = balance - monthlyMin # monthly unpaid balance
        balance = monthlyUnpaid + (monthlyInterest * monthlyUnpaid) # new balance carried over

    print ('Remaining balance:', round(balance, 2))

creditCard(balance, annualInterestRate, monthlyPaymentRate)

# monthly interest rate = annualInterestRate / 12.0
# minimum monthly payment = monthlyPaymentRate * previous balance
# monthly unpaid balance = previous balance - minimum monthly payment
# updated balance each month = monthly unpaid balance + (monthly interest rate * monthly unpaid balance)