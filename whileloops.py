#x = 0
#while x < 100:
#    print x
#   x += 1

#def countdown(x):
#    while x >= 0:
#        print x
#        x -= 1
#countdown(100)

#def countup(x):
#    if x > 0:
#        while x >= 0:
#            print x
#            x -= 1
#    else:
#        while x <= 0:
#            print x
#            x += 1
#countup(-10)

#def addup(x):
#    while x >= 0:
#        print x + (x-1)
#        x -= 1
#addup(10)

#def countfrom(x, y):
#    if x < y:
#        while x <= y:
#            print x
#            x += 1
#    else:
#        while y <= x:
#            print y
#            y += 1
#countfrom(-10,10)

def sum_of_odds(n):
    if n < 0:
            while n <= 0:
                print n
                n += 1
    else:
        while n >= 0:
            print n
sum_of_odds(10)
