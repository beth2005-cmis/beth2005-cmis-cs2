x= raw_input("type a number: ")
y= raw_input("type another: ")
z= int(x) + int(y)
print str(x) + "+" + str(y) + "=" + str(z)

prompt= 'What...is the airspeed velocity of an unladen swallow?\n'
speed= raw_input(prompt)
name= raw_input('What...is your name?\n')
print "Hey " + name + "!"

output= """
Hey {}
Did you know:
{} + {} = {}
{}
{}
""". format(name, x,y,z)
print output

import math
def qdr(a, b, c):
    return ((-b+math.sqrt(b**2-4*a*c))/2*a)

print output
def output(name, a, b, c, d):
    out= """
Hey {}
Did you know:
({}+math.sqrt{})/{})
""". format(name, a,b,c,d)

def main():
    name= raw_input("What's your name?:")
    a= raw_input("Favorite number1:")
    b= raw_input("Favorite number2:")
    c= raw_input("Favorite number3:")
    d= (int(-b)+math.sqrt(int(b)**2-4*int(a)*int(c))/2*int(a)
    out= output (name, a, b, c, d)
    print out

main()
