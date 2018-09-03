# Fibonacci function that returns the n amount of Fibonacci numbers
# The function check for input less than 1 (returns empty list), input equal to 1 (returns list with 1 value) and input greater than 1 (returns lst of size n with all Fibonacci numbers)
def fib(n):
	if n == 1:
		ls = [0]
	elif n > 1:
		# Fib sequence starting values
		ls = [0,1]
		
		# Looping up to n and calculating all required fib numbers
		for i in range(n-len(ls)):
			ls.append(ls[i] + ls[i+1])
	else:
		ls = []
	return ls

# Start of Fibonacci.py
print("## -- Fibonacci.py -- ##")
print("0 to exit")

digits = -1
str_base = "How many Fibonacci digits do you want?"
str = ""

# This while loop runs while input does not equal 0
while digits != 0:	
	# The try is to catch any invalid input (only integers allowed)
	try:
		# Asking for input
		digits = int(input(str+str_base))
		
		# Checking input value
		if digits < 0:
			str = "Please enter an integer greater than 0. "
		elif digits > 0:
			print(fib(digits))
			str = ""
		elif digits == 0:
			print("Goodbye!")
		else:
			str = "Please enter integers only. "
	except:
		str = "Please enter integers only. "
	