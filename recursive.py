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
def biggest(big):
    n = raw_input("Next number: ")   
    if n == "":
        print "The biggest number is " + str(big)
    else: 
        if big > float(n):
            biggest(big)
        else:
            biggest(float(n))
biggest(-float("inf"))

#smallest
def smallest(small):
    n = raw_input("Next number: ")   
    if n == "":
        print "The smallest number is " + str(small)
    else: 
        if small < float(n):
            smallest(small)
        else:
            smallest(float(n))
smallest(float("inf"))

#def smallest(number):
#	n = raw_input("Next number: ")
#    if n == "":
#        return number
#    else:
#        n = float(n)
#        if n < number;
#            number = n
#        return smallest(number)

#def pow(x, n):
#    if n == 0:
#        return 1
#    else:
#        return x * pow(x, n-1)
#pow(4, 4)

def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)

def countup(n):
	if n > 9:
		print "Blah"
	else:
		print n
		countup(n+1)

def countdown_from_to(start, stop):
	if start == stop:
		print "Something"
	else:
		print start
		countdown_from_to(start-1, stop)

def countup_from_to(start, stop):
	if start >= stop:
		print "SE"
	else:
		print start
		countup_from_to(start+1, stop)

def adder(total):
	print "Running total: {}".format(total)	
	n = raw_input("n: ")
	if n == "":			
		print "bye"
	else:
		total += int(n)
		adder(total)

def biggest(number):
	n = raw_input("Next number: ")
	if n == "":
		return number
	else:
		n = float(n)
		if n > number:
			number = n
		return biggest(number)


def smallest(number):
	n = raw_input("Next number: ")
	if n == "":
		return number
	else:
		n = float(n)
		if n < number:
			number = n
		return smallest(number)

def pow(x, n):
	if n == 0:
		return 1
	else:
		return x * pow(x, n-1)

