sum_of_squares = 0

for i in range(1, 101):
	sum_of_squares += i ** 2

square_of_sums = 0

for i in range(1, 101):
	square_of_sums += i

square_of_sums = square_of_sums ** 2
print "The difference is " + str(square_of_sums - sum_of_squares) + "."