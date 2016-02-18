import math
#add two arguments
def add(a, b):
    return a + b
print add(3,4)
#subtract two arguments
def sub(a, b):
    return a - b
print sub(5,3)
#multiply two arguments
def mul(a, b):
    return a * b
print mul(4,4)
#divide two arguments
def div(a, b):
    return float(a)/b
print div(2,3)
#number of seconds to number of hours
def hours_from_seconds(a):
    return float(a) / 3600
print hours_from_seconds(86400)
#one argument that represents the radius of a circle
def circle_area(a):
    return float(a)**2 * math.pi
print circle_area(5)
#one argument that represents the radius of a sphere
def sphere_volume(a):
    return (float(a)**3 * math.pi *4)/3
print sphere_volume(5)
#two integer or float arguments that represent the diameters of a sphere
def avg_volume(a, b):
    return ((((((float(a))/2)**3)*math.pi*4)/3)+(((((float(b))/2)**3)*math.pi*4)/3))/2
print avg_volume(10,20)
#three side lengths of a triangle as arguments
def area(a, b, c):
    return math.sqrt((((a+b+c)/2))*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))
print area(1,2,2.5)
#string as an argument and perfectly right aligned
def right_align(word):
    return (80-len(word))*" "+word
print right_align("Hello")
#string as an argument and returns that word with additional spaces
def center(word):
    return (40-len(word))*" "+word
print center("Hello")
#string as an argument and returns a message box
def msg_box(word):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word)+ (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"
print msg_box("Hello")
print msg_box("I eat cats!")
#call all the functions again
def add(a, b):
	return a + b
a = 3
b = 4
c = 4
d = 5
z = add(a, b)
x = add(c, d)
print msg_box(str(z)+", "+str(x))
def sub(a, b):
    return a - b
a = 5
b = 3
c = 6
d = 4
z = sub(a,b)
x = sub(c,d)
print msg_box(str(z)+", "+str(x))
def mul(a, b):
    return a * b
a = 4
b = 4
c =3
d =3
z = mul(a,b)
x = mul(c,d)
print msg_box(str(z)+", "+str(x))
def div(a, b):
    return float(a) / b
a = 2
b = 3
c = 3
d =4
z = div(a,b)
x = div(c,d)
print msg_box(str(z)+", "+str(x))
def hours_from_seconds(a):
    return a / 3600
z = hours_from_seconds(86400)
x = hours_from_seconds(90000)
print msg_box(str(z)+", "+str(x))
def circle_area(a):
    return float(a)**2 * math.pi
z = circle_area(5)
x = circle_area(10)
print msg_box(str(z)+", "+str(x))
def sphere_volume(a):
    return (float(a)**3 * math.pi *4)/3
z = sphere_volume(5)
x = sphere_volume(6)
print msg_box(str(z)+", "+str(x))
def avg_volume(a, b):
    return ((((((float(a))/2)**3)*math.pi*4)/3)+(((((float(b))/2)**3)*math.pi*4)/3))/2
z = avg_volume(10,20)
x = avg_volume(5,10)
print msg_box(str(z)+", "+str(x))
def area(a, b, c):
    return math.sqrt((((a+b+c)/2))*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))
z = area(1,2,2.5)
x= area(2,2,3.5)
print msg_box(str(z)+", "+str(x))
def right_align(word):
    return (60-len(word))*" "+word
z = right_align("Hello")
x = right_align("wasup")
print msg_box(z)
print msg_box(x)
def center(word):
    return (34-len(word))*" "+word
z = center("Hello")
x = center("wasup")
print msg_box(z)
print msg_box(x)
