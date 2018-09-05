import random
	
# Function to flip a coin a certain number of times and determine heads or tails
# Returns a list of 2 values with number of heads and number of tails	
def flip(n):
	maxRand = 100;
	ls = []
	heads = 0
	tails = 0
	for i in range(n):
		# The random.randint(1,N) returns a random integer between 1 and N
		if ((random.randint(1,maxRand)) > maxRand/2):
			heads += 1
		else:
			tails += 1
	ls.append(heads)
	ls.append(tails)

	return ls
	
## -- Start of coin flip --
## -- Assuming positive integer input

print("-- Start of coin flip --")
print("-- Assuming positive integer input")

# Getting input
n = input("How many flips?: ")

# Flipping coin
rs = flip(int(n))

# Printing results
print("Heads: " + str(rs[0]) + " - " + str(100*rs[0]/int(n)) + "%")
print("Tails: " + str(rs[1]) + " - " + str(100*rs[1]/int(n)) + "%")