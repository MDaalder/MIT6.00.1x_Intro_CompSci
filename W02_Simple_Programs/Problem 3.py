# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 02:26:50 2019

@author: Matt

This program usese bisection search to determine the lowest monthly payment, to the cent, that has to be made to
    pay off debts in one year, or any assigned number of months.
 
The lowBound for the search is assuming the balance is paid in x months equal payments, with no accruing monthly interest
The highBound for the search is assuming no monthly payments are made, and only one lump sum is made after x number of months
    of accruing interest. This gives us the highest possible final balance to pay off.
    
"""

# test case. Answer is 90325.03
# balance = 999999
# annualInterestRate = 0.18

def creditCard(balance, annualInterestRate):
    
    months = 12
    monthlyInterest = annualInterestRate/12.0
    lowBound = balance/months # low bound for bisection search
    highBound = (balance * (1 + monthlyInterest)**months)/months # high bound for bisection search
    monthlyMin = (lowBound + highBound)/2 # starting mid point value for bisection search
    balance0 = balance # dummy variable to maintain starting balance value
    
    def paymentLow(balance0, monthlyMin, lowBound, highBound): # takes in starting balance, monthly payment, and bounds for bisection search
            
        for i in range(months):
            
            monthlyUnpaid = balance0 - monthlyMin
            balance0 = monthlyUnpaid + (monthlyUnpaid * monthlyInterest) # remaining balance after x months of payments and interest
            
        if balance0 > 0.01: # if monthlyMin payments are too small
            
            lowBound = monthlyMin # assign new lowBound
            monthlyMin = (monthlyMin + highBound)/2 # assign new mid point
            balance0 = balance # reset the starting balance
                    
            return paymentLow(balance0, monthlyMin, lowBound, highBound)
            
        if balance0 < -0.01: # if monthlyMin payments are too large
            
            highBound = monthlyMin # assign new hihgBound
            monthlyMin = (monthlyMin + lowBound)/2 # assign new mid point
            balance0 = balance # reset the starting balance
           
            return paymentLow(balance0, monthlyMin, lowBound, highBound)
            
        else:
            return monthlyMin # returns the final monthlyMin payment to use (the answer)
    
    paymentLow(balance0, monthlyMin, lowBound, highBound)

    return paymentLow(balance0, monthlyMin, lowBound, highBound)#(balance, monthlyMin)  
    
creditCard(balance, annualInterestRate) # initiate function

print('Lowest Payment:', round(creditCard(balance, annualInterestRate),2)) # prints the answer