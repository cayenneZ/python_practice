# Reading files

from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % (filename))
print (txt.read())

print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())


# What does from sys import argv mean?
# For now, just understand that sys is a package, 
# and this phrase just says to get the argv feature
# from that package. You’ll learn more about these later.