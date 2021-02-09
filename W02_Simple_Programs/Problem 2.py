# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:42:11 2019

@author: Matt

Calculates the lowest monthly payment that will pay off all debt in 1 year.

Takes in initial balance, annual interest rate.

The monthly payment must be a multiple of $10.
Final balance may be a negative number.
"""

# this test should give answer 360
balance = 3926 #starting balance
annualInterestRate = 0.2 #percentage, divide by 12 for monthly interest rate

def creditCard(balance, annualInterestRate):

    months = 12 # number of months to calculate interest for
    monthlyInterest = annualInterestRate/12.0 #monthly interest rate
    monthlyMin = 10 # monthly minimum payment to pay off debt in a year
    balance0 = balance # dummy variable for balance, need to recall original balance at some point
    
    def paymentLow(balance0, monthlyMin):
        
        for i in range(months): #calculate outcome after 12 months of monthly interest and payments
                
            monthlyUnpaid = balance0 - monthlyMin # monthly unpaid balance
            balance0 = monthlyUnpaid + (monthlyInterest * monthlyUnpaid) # new balance carried over
           # print('balance0 is:', balance0, 'month is:', months) # check work
            
        if balance0 > 0: # if balance is still above 0
            monthlyMin += 10 # increase payments by $10 per month
            balance0 = balance # reset the dummy balance variable
            return paymentLow(balance0, monthlyMin) # return the new values back to the function and try again
        
        else:
            return monthlyMin # you've found your lowest monthly payment to pay off debt in 1 year
        
    paymentLow(balance0, monthlyMin) # initiate the function       
    
    return paymentLow(balance0, monthlyMin) # return value from function to creditCard function

creditCard(balance, annualInterestRate) # initiate the function

print ('Lowest Payment:', creditCard(balance, annualInterestRate)) # print the answer

# monthly interest rate = annualInterestRate / 12.0
# minimum monthly payment = monthlyPaymentRate * previous balance
# monthly unpaid balance = previous balance - minimum monthly payment
# updated balance each month = monthly unpaid balance + (monthly interest rate * monthly unpaid balance)