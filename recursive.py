def countdown(n):
    if n <= 0:
        print "Blastoff"
    else:
        print n
        countdown(n-1)

def count_down_from(start, stop):
    print count_down_from(10,5)

def main():
    countdown(5)
    return
main()


