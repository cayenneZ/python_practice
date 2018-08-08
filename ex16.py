# Reading and Writing Files

from sys import argv

script, filename = argv

print ("We're going to erase %r" % filename)
print ("If you don't want that, hit CTRL-C(^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Open the file...")

target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()


# the list of commands I want you to remember:
# close: Closes the fi le. Like File- >Save.. in your editor.
# read：Reads the contents of the file. You can assign the result to a variable.
# readline: Reads just one line of a text file.
# truncate: Empties the fi le. Watch out if you care about the file.
# write(stuff): Writes stuff to the file.