#My scrip is a math game. You are given five questions in three different stages. Your goal is to finish the given task. 

import math
import random

correct = 0
incorrect = 0

#Instructions before the game starts
print "You are given five questions in three different stages. For the sixth questions in each stages, press 'enter' to continue. Start the game right away."

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
        print "you got ", a_correct, " correct."
        print "You got ", a_incorrect, " incorrect."
    elif int(answer) == x + y:
        print("That's right!")
        a_correct += 1
        addition_question(x, y, times - 1, a_correct, a_incorrect)
    else: 
        print("That's wrong!")
        a_incorrect = a_incorrect + 1
        addition_question(x, y, times - 1, a_correct, a_incorrect) 
        return a_correct

def subtraction_question(x, y, times, s_correct, s_incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "-" + str(y))
    if times == 0:
        print "you got ", s_correct, " correct."
        print "You got ", s_incorrect, " incorrect."
    elif int(answer) == x - y:
        print("That's right!")
        s_correct += 1
        subtraction_question(x, y, times - 1, s_correct, s_incorrect)
    else: 
        print("That's wrong!")
        s_incorrect = s_incorrect + 1
        subtraction_question(x, y, times - 1, s_correct, s_incorrect) 

def multi_question(x, y, times, m_correct, m_incorrect):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "*" + str(y))
    if times == 0:
        print "you got ", m_correct, " correct."
        print "You got ", m_incorrect, " incorrect."
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

    total_c = a_correct + s_correct + m_correct
    total_i = a_incorrect + s_incorrect + m_incorrect 
    print "\nYou got a total number of ", total_c, " correct."
    print "You got a total number of ", total_i, " incorrect."
    if total_c <= total_i:
        print " PLEASE DON'T HATE MATH! MATH LIKES YOU"
    else:
        print "YOU HAVE NO LIFE BUT YOU'RE DOIND GREAT X)"
main()

