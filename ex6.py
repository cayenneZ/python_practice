x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2 string binary and do_not in "y"

print (x)
print (y)

print ("I said: %r." % x) # 'x' as a string in print function. got a "" by %r
print ("I also said: '%s'." % y) # 'y' as a string in print function.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious) # 'hilarious' as a string in 'joke_evaluation' in print function.

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)


# What is the difference between %r and %s?
# We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and
# others for displaying to users.
# What’s the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are for actually displaying variables to users.