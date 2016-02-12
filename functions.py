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
    return a / 3600
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
print add(3,4)
print sub(5,3)
print mul(4,4)
print div(2,3)
print hours_from_seconds(86400)
print circle_area(5)
print sphere_volume(5)
print avg_volume(10,20)
print area(1,2,2.5)
print right_align("Hello")
print center("Hello")
print msg_box("Hello")
print msg_box("I eat cats!")
print msg_box("output")
