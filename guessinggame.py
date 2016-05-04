import random.randint
1 <= random.randint <= 100

def guess(n, g_n):
    n = random.randint
    g_n = raw_input("Guess: ")
    if n == g_n:
        print "You're Awesome!"
        return guess(n, g_n)
    elif n < g_n:
        print "It's too big"
    elif n > g_n:
        print "It's too small"
    else:
        
