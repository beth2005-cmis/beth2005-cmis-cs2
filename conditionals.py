#This game is about testing your destiny, where you need to cut a rope that is not tied to you. You'll eventually die if you cut a wrong rope, but will be saved otherwise. 

import random
#conditional execution
#raw input
#relation operators
def intro():
	print "This is how the game goes"
	read = raw_input("Type to read carefully (yes/no):")
	if read == "yes" or read == "no":
		print "Please read the questions carefully, and follow instructions or else you'll DIE! <P.S.: don't use capital letters"
#str.format
#""" """
#relation operator
def start():
	name = raw_input("Who are you?:")
	if not name == "bob":
		print "Be prepared to test your destiny."
	out = """
You were caught by the pirates few days ago, and now you are tied to a chair in a ship, ready to be thrown away to be fed by crocodiles. {}, choose the right one to be freed.
""".format(name)
	print out
#chained conditionals
#return interger
def firsttry():
	print "In front of you, there are three ropes: long, medium, short."

	cut1 = raw_input("Type the length of the rope:")
	if cut1 == "long":
		cut1 = 1
		return cut1
	elif cut1 == "medium":
		cut1 = 2
		return cut1
	elif cut1 == "short":
		cut1 = 3
		return cut1
#chained conditionals
#return string
#relation operator
def ask_again(cut1):
	if cut1 > 1 and cut1 < 3:
		ask_again = raw_input("Are you sure? (yes/no):")
		if ask_again == "no":
			cut1 = raw_input("Type the length of the rope again:")
			if cut1 == "long":
				cut1 = 1
				return cut1
			elif cut1 == "medium":
				cut1 = 2
				return cut1
			elif cut1 == "short":
				cut1 = 3
				return cut1
		else:
			return cut1
#alternative execution
def destiny(cut1, oops):
	if str(cut1) == oops:
		print "AAAAAAAAH you're dead."
		exit()
	else:
		print "YAAASSSSS you did it! Do it one more time!"
#chained conditional
#conditional execution
#logical operators
def secondtry(oops):
	print "\nTwo ropes left... Choose another."
	cut2 = raw_input("Type the length of the rope:")
	if cut2 > int(oops) or cut2 < int(oops) or cut2 == int(oops):
		ask_again = raw_input("Are you sure? (yes/no):")
		if ask_again == "yes" or ask_again == "no":
			cut2 = raw_input("Type the length of the rope again:")
	if cut2 == "long":
		cut2 = 1
	elif cut2 == "medium":
		cut2 = 2
	elif cut2 == "short":
		cut2 = 3
#alternative execution
def destiny2(cut2, oops):
	if str(cut2) == oops:
		print "AAAAAAAAH you're dead."
	else:
		print "YAAASSSSS you did it!...but uh-oh... pirates decided to kill you anyways. BYEE"
#type conversion
#random.randint
#main
def main():
	import random
	oops = str(random.randint(1, 3))
	intro()
	start()
	cut1 = firsttry()
	ask_again(cut1)
	destiny(cut1, oops)	
	cut2 = secondtry(oops)
	destiny2(cut2, oops)
main()

#return boolean, flow control
v = raw_input("Guess a number from 1 ~ 3: ")
def guess_n(v):
    if v == 2:
        return True
guess_n(v)

if v:
    print "yes it's always 2"
else:
    print "you don't have a second chance"
