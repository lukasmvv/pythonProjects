# Returns the sum of gigits squared of a given number
def get_sum_of_squares(n):
	if n == 1:
		return 1
	else:
		num = 0
		for digit in str(n):
			num = num + (int(digit))**2
		return num
		
# Check to see if given number if happy or not		
def is_happy(n, temp_list, unhappy_numbers):
	num = get_sum_of_squares(n)
	
	# Happy condition
	if num == 1:
		return True
	
	# If part of previous unphappy sequence
	elif n in unhappy_numbers:
		return False
		
	# If number has been repeated
	elif n in temp_list:
		unhappy_numbers.append(temp_list)
		return False
	
	# Sequence has not reached 1 and has not started repeating
	else:
		temp_list.append(n)
		return is_happy(num, temp_list, unhappy_numbers)
			
print('-- Start of Happy Numbers ---')
happyToFind = int(input('Assuming positive integer input. How many happy numbers do you want? '))

loop = True
happy_numbers = []
unhappy_numbers = []
num_happy = 0
i = 0

while num_happy < happyToFind:
	temp_list = []
	if is_happy(i+1,temp_list, unhappy_numbers):
		happy_numbers.append(i+1)
		num_happy = num_happy + 1
	i = i + 1
print(happy_numbers)

	
