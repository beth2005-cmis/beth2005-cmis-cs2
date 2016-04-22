print "Running total: 0"

def adder():
    
    running_total = 0
    sum = next_number + running_total    
    
    next_number = float(raw_input("Next number: "))
    if next_number == " ":
        print "The sum is {}".format(sum)
    else:
        running_total = next_number + running_total
        print "Running total: {}".format(sum)
    return


