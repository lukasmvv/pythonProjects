## -- Start of FizzBuzz Example --

print("-- Start of FizzBuzz.py --")

for i in range(100):
	n = i + 1
	str1 = ""
	if n%3 == 0:
		str1 += "Fizz"
	if n%5 == 0:
		str1 += "Buzz"
	if str1 == "":
		str1 = str(n)
	print(str1)