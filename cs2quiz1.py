#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# "=" is used to put a value into a variable
# 
# +1point

#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that performs a computation. 
#
# +3point

#3 1pt) What does the keyword "return" do?
# "return" gives you the output of the function.
#
# +1point

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
#   ex) ("hi", "hello", 22, "hehe"), ("wassup", 15, "yo", "yoyo")
#
# +5point

#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is a statement that creates a new function, specifying its name, parameters, and the statements it executes. A function call is a statement that executes a function, and it consists of the funciton name followed by an argument list. 
#
# +2point

#6 3pts) What are the 3 phases that every computer program has? What happens in each of them
#	1: input -information supplied to the computer
#	2: processing -performing input 
#	3: output -infromation provided by the computer
#
# +3point

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

import math
def radiusFromArea(area):
    radius = math.sqrt(float(area)/math.pi)
    return radius
# +1 pt for header line
# +3 pt for correct formula
# +1 pt for return value
# +1 pt for parameter name
# +1 pt for function name

def output(d1, d2, d3, sumDiameters):
    out = """

""".format(d1,d2,d3,sumDiameters)
    return out
# +1pt for header line
# +1pt for parameter names
# +1pt for return value
# +0.5pt for correct output format
# +1pt for correct use of format function

def main():  
#input
    c1 = float(raw_input("area of c1: "))
    c2 = float(raw_input("area of c2: "))
    c3 = float(raw_input("area of c3: "))
#processing
    r1 = radius_from_Area(c1)
    r2 = radius_from_Area(c2)
    r3 = radius_from_Area(c3)

    d1 = r1*2
    d2 = r2*2
    d3 = r3*2    
    sumDiameters = d1 + d2 + d3
#output

main()
# +1pt header line
# +1pt getting input
# +1pt converting input
# +0.5pt for calling output function
# +2pt for correct diameter formula
# +1pt for variable names
# +1pt for calling main
# +1pt explanatory comments

