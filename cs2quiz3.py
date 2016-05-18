# 1) What is a recursive function?
# A function calls itself, meaning it will repeat itself when a certain line or a code is called.

# 2) What happens if there is no base case defined in a recursive function?
#It will recurse infinitely and maybe you will get an error that says your maximum recursion is reached.

# 3) What is the first thing to consider when designing a recursive function?
# You have to consider what the base case(s) are going to be because that is when and how your function will end and return something.

# 4) How do we put data into a function call?
# We put data into a function call by using parameters.

# 5) How do we get data out of a function call?
# We get data out of a function call by using parameters.


#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 = 4
#c3 = 45 

#d1 = 6
#d2 = 8
#d3 = 4

#Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def avg_odd_numbers(sum_n=0, odd_n=0):
    n = raw_input("Next number: ")
#Base Case
    if n == "":
        return "The average of all the odd numbers are {}".format(sum_n/odd_n)
#Recursive Case
    else:
        if float(n) % 2 == 1:
            return avg_odd_numbers(sum_n + float(n), odd_n + 1)
        else:
            return avg_odd_numbers(sum_n, odd_n)
print avg_odd_numbers()

