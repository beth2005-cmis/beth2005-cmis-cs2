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



