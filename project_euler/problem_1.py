"""A simple program that calculates the sum of all the multiples of 
3 and 5 less than 1000"""

# start with an incrementing variable
total = 0

# loop over every value between 1 and 1000 to check
for i in range(1, 1000):
	# perform the check
	if i % 3 == 0 or i % 5 == 0:
		total += i
	else:
		pass

# print the result to the screen		
print "The sum of all the multiples of 3 and 5 below 1000 is %s." % str(total)