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


def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    times = 5
    correct = 0
    incorrect = 0
    addition_question(x, y, times, correct, incorrect)
    subtraction_question(x, y, times, correct, incorrect)
main()



