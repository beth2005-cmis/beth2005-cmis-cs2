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
""". format(name, x,y,z,1,2)

print output

def out put (name,
