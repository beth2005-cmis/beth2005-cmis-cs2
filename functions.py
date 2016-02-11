import math
#add two arguments
def add(a, b):
    return a + b
c= add(3, 4)
print c
#subtract two arguments
def sub(a, b):
    return a - b
c= sub(5, 3)
print c
#multiply two arguments
def mul(a, b):
    return a * b
c= mul(4, 4)
print c
#divide two arguments
def div(a, b):
    return float(a)/b
c= div(2, 3)
print c
#number of seconds to number of hours
def hours_from_seconds(a, b):
    return a / b
c= div(86400, 3600)
print c
#one argument that represents the radius of a circle
def circle_area(a):
    return float(a)**2 * math.pi
c= 5**2 * math.pi
print c
#one argument that represents the radius of a sphere
def sphere_volume(a):
    return (float(a)**3 * math.pi *4)/3
c= (5**3 * math.pi * 4)/3
print c
#two integer or float arguments that represent the diameters of a sphere
def avg_volume(a, b):
    return ((((((float(a))/2)**3)*math.pi*4)/3)+(((((float(b))/2)**3)*math.pi*4)/3))/2
c= ((((((10)/2)**3)*math.pi*4)/3)+(((((20)/2)**3)*math.pi*4)/3))/2
print c
#three side lengths of a triangle as arguments
def area(a, b, c):
    return math.sqrt((((a+b+c)/2))*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))
c= math.sqrt((((1+2+2.5)/2))*(((1+2+2.5)/2)-1)*(((1+2+2.5)/2)-2)*(((1+2+2.5)/2)-2.5))
print c
print area(1,2,2.5)
#string as an argument and perfectly right aligned
def right_align(word):
    return ((80-len(word))*" "+word
