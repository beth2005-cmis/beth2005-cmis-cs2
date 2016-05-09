#My scrip is a math game. You are given five questions in four different stages. For each stages, if you miss more than three questions, then the game will restart for you. Your goal is to finish the last stage and happily go home. 

import math
import random

#Instructions before the game starts
input("Hit 'enter' to begin")

#Scores for each Stages
correct = 0
incorrect = 0

#List of question in Stage 1
def addition_questions():
    x = random.randint(1, 10)
    y = random.rantint(1, 10)
    return int('x + y')
print addition_questions
