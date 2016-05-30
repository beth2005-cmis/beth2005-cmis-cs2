#My scrip is a math game. You are given five questions in three different stages. Your goal is to finish the given task. 


v = raw_input("Are you pretty? ")
if v == "yes":
	print "YOU're actually ugly."

if v == "no":
    print "Das righ"
else:
    print "It's okay"

r = raw_input("Are you smart? ")
if v == "yes":
    print "YOU're actually dumb."

if r == "no":
    print "Das righ"
else:
    print "Let's test your IQ"

import math
import random

correct = 0
incorrect = 0

#Instructions before the game starts
print "You are given five questions in three different stages. Press 'enter' to ignore sixth question. Start the game right away."

a_correct = 0
a_incorrect = 0
s_correct = 0
s_incorrect = 0
m_correct = 0
m_incorrect = 0


def addition_question(x, y, times, a_correct, a_incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "+" + str(y))
    if times == 0:
        out ="""
You got {} correct.
\nYou got {} incorrect.
""".format(a_correct, a_incorrect)
        print out
    elif int(answer) == x + y:
        print("That's right!")
        a_correct += 1
        addition_question(x, y, times - 1, a_correct, a_incorrect)
    else: 
        print("That's wrong!")
        a_incorrect = a_incorrect + 1
        addition_question(x, y, times - 1, a_correct, a_incorrect) 


def subtraction_question(x, y, times, s_correct, s_incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "-" + str(y))
    if times == 0:
        out ="""
You got {} correct.
\nYou got {} incorrect.
""".format(s_correct, s_incorrect)
        print out
    elif int(answer) == x - y:
        print("That's right!")
        s_correct += 1
        subtraction_question(x, y, times - 1, s_correct, s_incorrect)
    elif answer == "":
        print("That's wrong!")
    else: 
        print("That's wrong!")
        s_incorrect = s_incorrect + 1
        subtraction_question(x, y, times - 1, s_correct, s_incorrect) 

def multi_question(x, y, times, m_correct, m_incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "*" + str(y))
    if times == 0:
        out ="""
You got {} correct.
\nYou got {} incorrect.
""".format(m_correct, m_incorrect)
        print out
    elif int(answer) == int(x * y):
        print("That's right!")
        m_correct += 1
        multi_question(x, y, times - 1, m_correct, m_incorrect)
    else: 
        print("That's wrong!")
        m_incorrect = m_incorrect + 1
        multi_question(x, y, times - 1, m_correct, m_incorrect)

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    times = 5
    addition_question(x, y, times, a_correct, a_incorrect)
    subtraction_question(x, y, times, s_correct, s_incorrect)
    multi_question(x, y, times, m_correct, m_incorrect)
main()

