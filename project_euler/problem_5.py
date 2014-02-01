evenly_divisible = False
i = 20

while evenly_divisible == False:
	for j in range(11, 21):
		if j in range(11, 20) and i % j != 0:
			i += 2
			break
		elif j == 20 and i % j == 0:
			evenly_divisible = True
			break
		else:
			print(i)
			pass

print "The smallest positive # that is evenly divisible by all of the numbers from 1 to 20 is " + str(i) + "."