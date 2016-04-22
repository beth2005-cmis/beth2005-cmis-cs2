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
