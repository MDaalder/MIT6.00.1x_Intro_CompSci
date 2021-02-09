# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:56:03 2019

@author: Matt
"""
import pylab as plt

""" take monthly savings, annual interest rate, 
and how many terms/months to save for"""

def retire(monthly, rate, terms):
    savings = [0] # amount saved
    base = [0] # x values in months
    mRate = rate/12 # monthly rate of interest
    for i in range(terms): 
        base += [i]
        savings += [savings[-1]*(1 + mRate) + monthly]
    return base, savings


""" This will plot retirement outcomes by different monthly savings rates.
Monthlies are different amounts to put aside each month, as a list.
Rate is annual interest rate, terms is months to save for"""

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    plt.title('Retirement Savings by Monthly Contributions')
    plt.xlabel('Months of Savings')
    plt.ylabel('Savings in $')
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals,
                 label = 'retire:'+ '$'+str(monthly))
        plt.legend(loc = 'upper left')
        
displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40* 12)


""" This will plot retirement outcomes by different annual interest rates.
Rates are different annual interest rates, input as a list.
Month is how much saved each month, terms is months to save for"""

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    plt.title('Retirement Savings by Interest Rate')
    plt.xlabel('Months of Savings')
    plt.ylabel('Savings in $')
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals,
                 label = 'retire:'+ '$' + str(month)+ ':' + \
                 str(int(rate*100))+'%')
        plt.legend(loc = 'upper left')

displayRetireWRates(800, [.03, .05, .07], 40* 12)


#def displayRetireWMonthsAndRates(monthlies, rates, terms):
#    plt.figure('retireBoth')
#    plt.clf()
#    plt.xlim(30*12, 40*12) # only see savings outcomes near retirement
#    plt.title('Retirement Savings by Monthly Contribution and Interest Rate')
#    plt.xlabel('Months of Savings')
#    plt.ylabel('Savings in $')
#    for monthly in monthlies:
#        for rate in rates:
#            xvals, yvals = retire(monthly, rate, terms)
#            plt.plot(xvals, yvals, 
#                     label = 'retire:' + '$' + str(monthly) + ':' \
#                     + str(int(rate*100)) + '%')
#            plt.legend(loc = 'upper left')
#            
#displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)


""" This displays both data for monthly savings rates, and different
annual interest rates, combining the methods from above programs"""

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12) # only see savings outcomes near retirement
    plt.title('Retirement Savings by Monthly Contribution and Interest Rate')
    plt.xlabel('Months of Savings')
    plt.ylabel('Savings in $')
    
    # following creates a set of labels
    # we've set the same number of colours and styles to
    # the same number of monthly rates and terms give (4, and 3, respectively)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        # pick new label for each month choice
        monthLabel = monthLabels[i%len(monthLabels)]
        
        for j in range(len(rates)):
            rate = rates[j]
            # pick new label for each rate choice
            rateLabel = rateLabels[j%len(rateLabels)]
            
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                     monthLabel+rateLabel, #creates a new label for the plot
                     label = 'retire:' + '$' + str(monthly) + ':' \
                     + str(int(rate*100)) + '%')
            plt.legend(loc = 'upper left')
    
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)