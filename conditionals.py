#My scrip is a math game. You are given five questions in four different stages. For each stages, if you miss more than three questions, then the game will restart for you. You only have 2 minutes to answer these questions. Your goal is to finish the last stage and happily go home. 

import math
import random
import time

#Scores for each Stages
correct = 0
incorrect = 0

#List of question in Stage 1
def addition_questions(

#Instructions before the game starts
print("You have 20 seconds to finish Stage 1.")
input("Hit 'enter' to begin")

#start the timer
start = time.time()
print("The clock has started!!")

#List of questions
for q in questions:
    #display question and get answer
    answer = response(q + ": ", ['t','f']) == 't'
    result = eval(q)
    #compare answer to actual result
    if answer == result:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
    print(q + " is " + str(result) + "\n\n")
end = time.time()

#Results
print("Your time was: ", end - start, " seconds")
print("You got ", correct, " correct.")
print("You got ", incorrect, " incorrect.")
if incorrect > 0:
    print("Restart")
else:
    print("You passed, so go HOME!")
