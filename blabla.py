import random
import math

correct = 0
incorrect = 0

def addition_question1(x, y):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    answer = raw_input(str(x) + "+" + str(y))
    actual_answer = x + y
    if answer == actual_answer:
        print("That's right!")
        correct += 1
        return addition_question1(x, y)
    elif 
        print("That's wrong!")
        incorrect += 1
        addition_question1(x, y)

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    addition_question1(x, y)
main()

def addition_question2():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print raw_input(str(x) + "+" + str(y))
    answer2 = raw_input(str(x) + "+" + str(y))
    actual_answer2 = x + y
    if answer2 == actual_answer2:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
        addition_question2()

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    addition_question1(x, y)
main()

def addition_question3():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print raw_input(str(x) + "+" + str(y))
    answer3 = raw_input(str(x) + "+" + str(y))
    actual_answer3 = x + y
    if answer3 == actual_answer3:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
        addition_question3()

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    addition_question1(x, y)
main()

def addition_question4():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print raw_input(str(x) + "+" + str(y))
    answer4 = raw_input(str(x) + "+" + str(y))
    actual_answer4 = x + y
    if answer4 == actual_answer4:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
        addition_question4()

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    addition_question1(x, y)
main()

def addition_question5():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print raw_input(str(x) + "+" + str(y))
    answer5 = raw_input(str(x) + "+" + str(y))
    actual_answer5 = x + y
    if answer5 == actual_answer5:
        print("That's right!")
        correct += 1
    else:
        print("That's wrong!")
        incorrect += 1
        addition_question5()

def main():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    addition_question1(x, y)
main()

print "You got ", correct, " correct."
print "You got ", incorrect, " incorrect."
if incorrect > 2:
    print "game over"
else:
    print "You passed!"
