import math
import random

print"""
This program will ask you for 5 interger or float values. 
It will calculate the average of all values from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd.
"""

def main():
    amount = 0    
    #input
    n0= float(raw_input("n0 "))
    n1= float(raw_input("n1 "))
    n2= float(raw_input("n2 "))
    n3= float(raw_input("n3 "))
    n4= float(raw_input("n4 "))
    #processing
    average = (n0 + n1 + n2 + n3 + n4)/5
    #output
    if n0 > 0 and n0 < 10:
        total = amount += 1
    else:
        total = amount
        print n0, " is out of range."
    if n1 > 0 and n1 < 10:
        total = amount += 1
    else:
        total = amount
        print n1, " is out of range."
    if n2 > 0 and n2 < 10:
        total = amount += 1
    else:
        total = amount
        print n2, " is out of range."
    if n3 > 0 and n3 < 10:
        total = amount += 1
    else:
        total = amount
        print n3, " is out of range."
    if n4 > 0 and n4 < 10:
        total = amount += 1
    else:
        total = amount
        print n4, " is out of range."

