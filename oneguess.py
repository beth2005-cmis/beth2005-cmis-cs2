Sample Output:
What is the minimum number? 5
What is the maximum number? 10
I'm thinking of a number from 5 to 10.
What do you think it is?: 7

The target was 9.
Your guess was 7.
That's under by 2.

input random

def any_number():
    number = int(raw_input("Guess the number (5-10):")
    if number > 10 or number < 5:
        number = random.randint(5, 10)
    any_number = float(number)
    return any_number
