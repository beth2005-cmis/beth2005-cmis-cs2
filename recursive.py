#count down
def countdown(n):
    if n <= 0:
        print "Blastoff"
    else:
        print n
        countdown(n-1)

def count_down_from(start, stop):
    if start < stop:
        print "TEEHEE"
    else:
        print start
        count_down_from(start - 1, stop)
count_down_from(10, 1)

#count up
def countup(start, stop):
	if start > stop:
		print "TEEHEE"
	else:
		print start
		countup(start + 1, stop)
countup(1, 10)

#adder
def adder(s, total):
    if s == "":
        return total
    else:
        total += float(s)
        s = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(s, total)

def main():
    out = adder(0, 0)
    print "The sum is " + str(out)
main()

#biggest
def biggest(n, biggest):
    if n == "":
        return biggest
    elif n >= biggest:
        n = biggest
        return biggest    
    else: 
        n = raw_input("Next number: " + str(n) + "\nNext number: ")
        return n

def main():
    out = biggest(0, 0)
    print "The biggest number is " + str(out)
main()


#smallest

#pow


