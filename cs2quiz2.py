#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) not 1=1
#b) 1<2 or 4>5
#c) 2=2 and 2<1

#
#2) What does 'return' do?
# In computer programming, the 'return' executes the input of the function.
#
#

#3) What are 2 ways indentation is important in python code?
#a) tells you where the function end
#b) if it's not indented, it is not part of the function
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -6
#problem1_b) - square root of 3
#problem1_c) 0
#problem1_d) 
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import math

def main():
    #Input    
    name= raw_input("What's your name?:")
    a= float(raw_input("Type the first number:"))
    b= float(raw_input("Type the second number:"))
    c= float(raw_input("Type the third number:"))
    #Processing  
    #Output  
    if a > b and a > c:
        out = str(a) + "is the largest of the three numbers."
    elif b >= c or b <= c:
        out = "You did not follow directions"
    elif b > a and b > c:
        out = str(b) + "is the largest of the three numbers."
    elif a >= c or a <= c:
        out = "You did not follow directions"
    elif c > a and c > b:
        out = str(c) + "is the largest of the three numbers."
    elif a >= b or a <= b:
        out = "You did not follow directions"
    else:
        out = "You did not follow directions"

    print out
main()
