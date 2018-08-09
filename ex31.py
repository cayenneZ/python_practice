# Making Decisions

print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print ("There is a giant bear here eating a cheese cake. What do you do?")
	print ("1. Take the cake.")
	print ("2. Screan at the bear.")
	
	bear = input("> ")
	
	if bear == "1":
		print ("The bear eats your face off. Good job!")
	elif bear == "2":
		print ("The bear eats your legs off. Good job!")
	else:
		print ("Well doing %s is probably better. Bear runs away." % bear)
elif door == "2":
	print ("You")
	print ("1")
	print ("2")
	print ("3")
	
	insanity = input ("> ")
	
	if insanity == "1" or insanity == "2":
		print ("You body")
	else:
		print("The insanity rots your eyes into a pool of muck. Good job!")
else:
	print ("You stumble around and fall on a knife and die. Good job!")
	
	
# How do I tell if a number is between a range of numbers?
# You have two options: 
#	Use 0 < x < 10 or 1 <= x < 10, which is classic notation, 
#	or use x in range(1, 10).