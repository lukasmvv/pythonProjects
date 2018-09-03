def fib(n):
	x = 0
	y = 1
	ls = [x,y]
	for i in range(n):
		ls.append(next_fib(ls[i],ls[i+1]))
	return ls
def next_fib(x,y):
	return x + y

print("## -- Fibonacci.py -- ##")
digits = input("How many Fibonacci digits do you want?")
print(fib(int(digits)))