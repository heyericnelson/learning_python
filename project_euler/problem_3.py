from sys import argv

script, number = argv

number = int(number)

def find_largest_prime_factor(number):
	"""This function finds the largest prime factor of a number that the
	user passes to it."""
	
	largest = 1
	i = 1
	
	while i <= number:
		if is_prime(i) == True:
			if number % i == 0:
				largest = i
				i += 2
				print i - 2
			else:
				i += 2
		else:
			i += 2
	
	print "The largest prime factor of %i is %i." % (number, largest)
	
def is_prime(number):
	"""This function determines whether a given number is prime."""
	is_prime = True
	i = 2
	
	while i < (number ** (1/2) + 1) and is_prime == True:
		if number % i == 0:
			is_prime = False
			break
		else:
			i += 1
	
	return is_prime

find_largest_prime_factor(number)