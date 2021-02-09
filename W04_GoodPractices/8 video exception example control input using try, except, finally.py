# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:38:17 2019

Input from example is test grades of students (name, grade)
Outputs a list of lists

@author: Matt
"""

data = []

file_name = input('Provide a name of a file of data')

try:
    fh = open(file_name, 'r')
    
except IOError:
    print('Cannot open', file_name)
    
else:
    for new in fh:
        if new!= '\n':
            addIt = new[:-1].split(',') # remove trailing \n
            data.append(addIt)
            
finally:
    fh.close() #close file even if fail
            
# this output will have structure [[name, last name, grade], []]
    
# the following code creates 2 lists, one of the student names, one of the grades
# however, this code fails if the name isn't of structure 1st name, last name (i.e. 1 word names, 3 word names)
    
#gradesData = []
#
#if data:
#    for student in data:
#        try:
#            gradesData.append([student[0:2], [student[2]]]) # creates a list of names, and a list of grades
#        except IndexError: # if there is no grade for the student
#            gradesData.append([student[0:2], []]) # adds the student name, and empty list for the grade
#

# the following codes creates 2 lists, one of the stduent names, one of the grades
# works for all length of names

gradesData = []

if data:
    for student in data:
        try:
            name = student[0:-1] # everything but the grade, which is the last element
            grades = int(student[-1])
            grades.Data.append([name, [grades]])
        except ValueError: # if last element is not a grade, example: it is empty (no grade)
             gradesData.append([stduent[:], []])

            
                