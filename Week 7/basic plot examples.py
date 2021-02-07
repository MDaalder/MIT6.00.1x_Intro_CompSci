# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:41:26 2019

@author: Matt
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
    
# first trial
# overlapping graphs/plots    
# plt.plot(x values, y values)
# If done in console, opens a separate window. 
# If done in IPython console, will display inside that window.
plt.plot(mySamples, myLinear) 
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)


# second trial
# different names for plots, in different windows

plt.figure('lin')
plt.xlabel('sample points') #x label
plt.ylabel('linear function')#y label
plt.plot(mySamples, myLinear) 
plt.figure('quad')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cubic')
plt.plot(mySamples, myCubic)
plt.figure('exp')
plt.plot(mySamples, myExponential)

plt.figure('lin') # reopens figure assigned to 'lin'
plt.title('Linear') # assignes a title to figure 'lin'

""" the following clears the window 'lin'
comment it out to keep the changes to 'lin' made earlier """ 
plt.clf() # this clears the current window ('lin' in this case) so new values can be assigned to it

""" Comparing graphs, setting a limit to y axis"""
plt.figure('lin')
plt.clf()
plt.ylim(0, 1000) # puts a limit on y axis
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)

plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')

""" Overlaying plots and adding legends"""
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, label = 'Linear')
plt.plot(mySamples, myQuadratic, label = 'Quadratic')
plt.legend(loc = 'upper left') # set the location of the legend (labels in lines above)
plt.legend() # assigns the legend without manually setting a location
plt.title('Linear vs. Quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.title('Cubic vs. Exponential')


