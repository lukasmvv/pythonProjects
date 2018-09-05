# Method to return factorial of given integer input using loops
def fact_loop(n):
	ret = 1
	if n != 0 and n > 0:
		for i in range(n):
			ret = ret*(i+1)
	return ret
	
# Method to return factorial of given integer input using recursion
def fact_rec(n):
	if (n == 1 or n == 0):
		return 1
	else:
		return n*fact_rec(n-1)
	
	
## -- Start of Factorial Program -- #
print("-- Factorial.py --")
print("-- Assuming positive integer input --")

# Getting input
n = input("Enter integer: ")

# Calling loop and recursive methods
loop_fact = fact_loop(int(n))
rec_fact = fact_rec(int(n))

# Printing results
print("Factorial Loop: "+str(loop_fact))
print("Recursive Loop: "+str(rec_fact))

# Checking results are the same
if loop_fact == rec_fact:
	print("PASS")
else:
	print("FAIL")
