# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:23:43 2019

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


""" Changing display style.
Colour, display type, line thickness.
Subplots, legends"""
plt.figure('lin quad')
plt.clf()
# sublot: 2 rows, 1 column, use the 1 location
plt.subplot(211)
plt.ylim(0, 900)
# string b- specifies colour blue (b), style of a line (-), linewidth of 2.0
plt.plot(mySamples, myLinear, 'b-', label = 'Linear', linewidth = 2.0)
# subplot 2 rows, 1 column, use the 2 location
plt.subplot(212)
plt.ylim(0, 900)
# string specifies colour red (r), style of circles (o)
plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth = 3.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs. Qudaratic')

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
# string specifies colour green (g), style of triangles (^)
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 4.0)
plt.legend()

plt.subplot(122)
plt.ylim(0, 140000)
# string specifies colour red (r), style of dashed line (--)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth = 5.0)
plt.legend()
plt.title('Cubics vs. Exponential')



""" Changing the axis scale"""
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth = 5.0)
# the following makes the y axis a log scale
plt.yscale('log')
plt.legend()
plt.title('Cubic vs Exponential')

plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth = 5.0)
plt.legend()
plt.title('Cubic vs Exponential')
