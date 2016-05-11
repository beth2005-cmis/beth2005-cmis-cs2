#My scrip is a math game. You are given five questions in four different stages. For each stages, if you miss more than three questions, then the game will restart for you. Your goal is to finish the last stage and happily go home. 

import math
import random

correct = 0
incorrect = 0

#Instructions before the game starts
input("Hit 'enter' to begin")

def addition_questions():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = raw_input(str(x) + "+" + str(y))
    actual_answer = x + y
    if answer == actual_answer:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer2 = raw_input(str(x) + "+" + str(y))
    actual_answer2 = x + y
    if answer2 == actual_answer2:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer3 = raw_input(str(x) + "+" + str(y))
    actual_answer3 = x + y
    if answer3 == actual_answer3:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer4 = raw_input(str(x) + "+" + str(y))
    actual_answer4 = x + y
    if answer4 == actual_answer4:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer5 = raw_input(str(x) + "+" + str(y))
    actual_answer5 = x + y
    if answer5 == actual_answer5:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1

print "You got ", correct, " correct."
print "You got ", incorrect, " incorrect."
if incorrect > 2:
    print "game over"
else:
    print "You passed!"
