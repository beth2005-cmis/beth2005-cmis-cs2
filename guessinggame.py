import random

def guess(n, total_pt):

    g_n = int(raw_input("Guess: "))
    if g_n == n:
        print "You got " + str(total_pt) + " wrong!"
    elif g_n == n:
        print "You're Awesome!"
    elif g_n > n:
        print "It's too big"
        guess(n, total_pt + 1)
    else:
        print "It's too small"
        total_pt + 1
        guess(n, total_pt + 1)

guess(random.randint(1, 10), 0)
