#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# "=" is used to put a value into a variable
#
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that performs a computation. 
#
#
#3 1pt) What does the keyword "return" do?
# "return" gives you the output of the function.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two examples of each below
#	1: boolean ('bool')
#ex) True, False
#	2: integer ('int')
#   ex) 0, 1
#	3: floating point ('float')
#   ex) 0.0, 0.1
#	4: string ('str')
#   ex) "hello, world", "python"
#	5: tuple ('tuple')
#   ex) ("hi", "hello", 22, "hehe")
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is a statement that creates a new function, specifying its name, parameters, and the statements it executes. A function call is a statement that executes a function, and it consists of the funciton name followed by an argument list. 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in each of them
#	1:
#	2:
#	3:
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

def main():  
    prompt = 'what are the areas of 3 circles?\n' 
#Circle  Diameter
    c1 = raw_input("type a number: ")
    c2 = raw_input("type second number: ")
    c3 = raw_input("type third number: ")
    totals = int(c1) + int(c2) + int(c3)
    print prompt + totals

import math
def circle_area(radius1, radius2, radius3):
    area= float(radius)**2 * math.pi
    return area
print circle_area()

def sum_of_diameters(diameter1, diameter2, diameter3):
    circle_area
    c1 = diameter1/2
    c2 = diameter2/2
    c3 = diameter3/2
    total = c1 + c2 + c3
    return total
