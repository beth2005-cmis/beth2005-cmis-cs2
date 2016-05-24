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

def addup(x):
    while x >= 0:
        print x + (x-1)
        x -= 1
addup(10)
