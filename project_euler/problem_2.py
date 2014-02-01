def fibonacci_sum(maximum):
	"""The purpose of this function is to calculate the sum
	of the terms of the fibonacci sequence up to the 'maximum' value."""
	
	current_number = 1
	total = 0
	number_one = 1
	number_two = 2
	
	while current_number < maximum:
		if current_number % 2 == 0:
			total += number_two
	
		current_number = number_one + number_two
		number_one = number_two
		number_two = current_number
		
	return total
		
print "The total is %i." % fibonacci_sum(4000000)