def biggest(n, biggest):
    if n == "":
        return biggest
    elif n >= biggest:
        n = biggest
        return n    
    else: 
        n = raw_input("Next number: " + str(n) + "\nNext number: ")
        return biggest(n, biggest)


def main():
    out = biggest(0, 0)
    print "The biggest number is " + str(out)
main()

