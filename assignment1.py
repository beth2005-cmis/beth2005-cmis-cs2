#create a variable
myName= "Beth Jung"
#create a variable
myAge= 16.9
#create a variable
myHeight= 1.66
#create a variable
lSquare= 1
#create a variable
lRectangle= 2
#create a variable
hRectangle= 1
#compute the age in months
ageInMonths= myAge * 12
#compute the years to live
yearsToLive= myAge + ageInMonths
#compute the height in feet
heightInFeet= myHeight * 3.28
#compute the differences in height
differenceInHeight= myHeight - 1.60
#compute the area of a square
sArea= lSquare * lSquare
#compute half of the volume of the cube
hcVolume= 0.50 * sArea * lSquare
#compute one ninths of the volume of the rectangle
nrVolume= 0.11 * lRectangle * hRectangle
#create a variable
smileyFace= ";)"
#compute the numbers of the smileyFaces
smileyFaces= smileyFace * int(10000)
#Print out a message
print "Hello. My name is " + myName + "." + " I am " + str(myHeight) + " meters tall, or " + str(heightInFeet) + " tall in feet. I am " + str(myAge) + " years old so I have apporximately " + str(yearsToLive) + "years remaining in my life..."
#Print out a message
print "I have a square that is ", lSquare, "centimeter long." + "So, the area of the square would be ", sArea, "centimeter squared." + "Half of a volume of the cube would be ", hcVolume, "centimeters cubed." + "I also have a rectangle with ", lRectangle, "centimeters long, and ", hRectangle, "centimeters wide." 
#Print out a message
print smileyFaces
