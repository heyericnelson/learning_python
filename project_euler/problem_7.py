counter = 0
i = 2
prime_limit = 10001

def is_prime(number):
	"""This function determines whether a given number is prime."""
	is_prime = True
	i = 2
	
	while i < number and is_prime == True:
		if number % i == 0:
			is_prime = False
			break
		else:
			i += 1
	
	return is_prime

while counter < prime_limit:

	if is_prime(i) == True:
		counter += 1
		if counter == prime_limit:
			print "The " + str(prime_limit) + " prime is " + str(i) + "."
		else:
			print counter
			i += 1
	else:
		i += 1