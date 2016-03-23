import math

def qdr(a, b, c):
    d = abs((b**2) - (4*a*c))
    return (-b+math.sqrt(d))/(2*a)


def output(name, a, b, c, d):
    out= """
Hey {}
Did you know that the x is:
{}
""". format(name, d)
    return out

def main():
    name= raw_input("What's your name?:")
    a= float(raw_input("Favorite number1:"))
    b= float(raw_input("Favorite number2:"))
    c= float(raw_input("Favorite number3:"))
    d= qdr(a, b, c)
    out= output(name, a, b, c, d)
    print out
main()
