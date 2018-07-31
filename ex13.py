from sys import argv 

# the ex13.py part of the command is called an “argument.”  
# What we’ll do now is write a script that also accepts arguments

script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

# From now on we will be calling these “features” 
# that we import modules. I’ll say things like, 
# “You want to import the sys module.” They are 
# also called “libraries” by other programmers, 
# but let’s just stick with modules.