#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:57:52 2025

@author: chasecantrell
"""

# File: tuition.py
#
# Purpose: Calculates the tuition of a university ten years
# from now as well as the cost of a student's
# tuition for their four year career assuming that
# the student starts their career ten years from now.
# Prints out the tuition ten years from now and the
# student's total tuition.
#
# Programmer:Chase

# initialize variables appropriately for counting
tuition = 10000.00
count = 1
# using a while loop , calculate what the tuition will
# be in 10 years
while count <= 10:
    tuition = tuition * 1.05
    count = count + 1
# end while loop
# print out what the tuition will be in 10 years
print('Tuition in ten years will be $',
      format(tuition, ',.2f'))

# print out what the tuition will be for the
# first year for a student starting college
# in 10 years
sum = tuition
print('\nYear 1: $', format(sum, ',.2f'))
# calculate years 2 through 4 for the tuition
# for loop
for i in range(2,5,1):
    tuition = tuition * 1.05
    sum = sum + tuition
    print('Year', i, ':$', format(sum, ',.2f'))
# print out what the four year tuition will be
print('\nFour year tuition in ten years will be $',
      format(sum, ',.2f'))
# in ten years
# print message to end program
print('Made by chase')
