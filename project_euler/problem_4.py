outer_max = 999
found_palindrome = False
highest = 0

while outer_max >= 100 and found_palindrome = False:
	for i in range(0, outer_max):
	
		current_number = str(outer_max * (outer_max - i))
		reversed = reverse(current_number)
		
		if current_number == reverse(current_number):
			highest = int(current_number)
		else:
			pass
			
		

def reverse(s):
	"""This function is designed to reverse a string."""
	new = []
	
	for i in range(1, len(s)):
		new[i - 1] = s[-i]
	
	return new