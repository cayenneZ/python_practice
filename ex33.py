i = 0
numbers = []

while i < 6:
	print ("At the top i is %d" % i)
	numbers.append(i)
	
	i = i + 1
	print ("Numbers now:", numbers)
	print ("At the bottom i is %d" % i)
	
print ("The numbers:")

for num in numbers:
	print (num)
	
	





"""
try:
	print ("Hello World!")
	
except IOError:
    print('An error occured trying to read the file.')
    
except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print "NO module found"
    
except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')

except:
    print('An error occured.')
	"""