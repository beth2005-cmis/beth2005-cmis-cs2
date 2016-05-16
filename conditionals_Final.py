#My scrip is a math game. You are given five questions in four different stages. Your goal is to finish the given task. 

import math
import random

correct = 0
incorrect = 0

#Instructions before the game starts
print "You are given five questions in four different stages. For the sixth questions in each stages, press 'enter' to continue."
input("Hit 'enter' to begin")

import random
import math

correct = 0
incorrect = 0


def addition_question(x, y, times, correct, incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "+" + str(y))
    if times == 0:
        print "you got ", correct, " correct."
        print "You got ", incorrect, " incorrect."
    elif int(answer) == x + y:
        print("That's right!")
        correct += 1
        addition_question(x, y, times - 1, correct, incorrect)
    else: 
        print("That's wrong!")
        incorrect = incorrect + 1
        addition_question(x, y, times - 1, correct, incorrect)
    correct = a_correct
    incorrect = a_incorrect

def subtraction_question(x, y, times, correct, incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "-" + str(y))
    if times == 0:
        print "you got ", correct, " correct."
        print "You got ", incorrect, " incorrect."
    elif int(answer) == x - y:
        print("That's right!")
        correct += 1
        subtraction_question(x, y, times - 1, correct, incorrect)
    else: 
        print("That's wrong!")
        incorrect = incorrect + 1
        subtraction_question(x, y, times - 1, correct, incorrect)
    correct = s_correct
    incorrect = s_incorrect

def division_question(x, y, times, correct, incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "/" + str(y))
    if times == 0:
        print "you got ", correct, " correct."
        print "You got ", incorrect, " incorrect."
    elif float(answer) == x / y:
        print("That's right!")
        correct += 1
        division_question(x, y, times - 1, correct, incorrect)
    else: 
        print("That's wrong!")
        incorrect = incorrect + 1
        division_question(x, y, times - 1, correct, incorrect)
    correct = d_correct
    incorrect = d_incorrect

def multi_question(x, y, times, correct, incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "*" + str(y))
    if times == 0:
        print "you got ", correct, " correct."
        print "You got ", incorrect, " incorrect."
    elif int(answer) == x * y:
        print("That's right!")
        correct += 1
        multi_question(x, y, times - 1, correct, incorrect)
    else: 
        print("That's wrong!")
        incorrect = incorrect + 1
        multi_question(x, y, times - 1, correct, incorrect)
    correct = m_correct 
    incorrect = m_incorrect

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    times = 5
    correct = 0
    incorrect = 0
    addition_question(x, y, times, correct, incorrect)
    subtraction_question(x, y, times, correct, incorrect)
    division_question(x, y, times, correct, incorrect)
    multi_question(x, y, times, correct, incorrect)

    total_c = a_correct + s_correct + d_correct + m_correct
    total_i = a_incorrect + s_incorrect + d_incorrect + m_incorrect 
    print "You got a total number of ", total_c, " correct."
    print "\nYou got a total number of ", total_i, " incorrect."
    if total_c <= total_i:
        print "DON'T HATE MATH! MATH LIKES YOU"
    else:
        print "YOU HAVE NO LIFE BUT YOU'RE DOIND GREAT X)"
main()

