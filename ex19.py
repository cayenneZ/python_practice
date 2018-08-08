def cheese_and_crackers(cheese_count, boxer_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxes of crackers!" % boxer_of_crackers)
	print ("Man that's enough for a party!")
	print ("Get a blanket.\n")
	
print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print ("Or, We can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def apple_and_banana(apple_count, banana_count):
	print ("You have %d apples!" % apple_count)
	print ("You have %d bananas!" % banana_count)
	print ("\n")
apple_and_banana(10, 20) #1

apple_amount = 25
banana_amount = 35
apple_and_banana(apple_amount, banana_amount) #2

apple_and_banana(10, banana_amount) #3

apple_and_banana(apple_amount, 20) #4

apple_and_banana(10 + 20, 25 + 35) #5

apple_and_banana(10 + apple_amount, 20) #6

apple_and_banana(10, 20 + banana_amount) #7

apple_and_banana(10 + apple_amount, 20 + banana_amount) #8

apple_and_banana(apple_amount, 20 + banana_amount) #9

apple_and_banana(10 + apple_amount, banana_amount) #10
