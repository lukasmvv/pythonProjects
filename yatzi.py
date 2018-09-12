# This program plays the classic Yatzi game
# Author: Lukas van Vuuren

import random

# ----- Player Class -----
class player:

	# Class variables
	totalScore = 0
	bonusScore = 0
	amountOdDi = 5
	
	# This is the initialise constructor. Self refers to the instance of the class
	def __init__(self, name, oneScore, twoScore, threeScore, fourScore, fiveScore, sixScore, tripleScore, quadScore, fullHouseScore, shortScore, longScore, yatziScore, chanceScore, rolledDi, keptDi):
		self.name = name
		self.oneScore = oneScore
		self.twoScore = twoScore
		self.threeScore = threeScore
		self.fourScore = fourScore
		self.fiveScore = fiveScore
		self.sixScore = sixScore
		self.tripleScore = tripleScore
		self.quadScore = quadScore
		self.fullHouseScore = fullHouseScore
		self.shortScore = shortScore
		self.longScore = longScore
		self.yatziScore = yatziScore
		self.chanceScore = chanceScore
		self.rolledDi = rolledDi
		self.keptDi = keptDi
		
		player.amountOdDi = 5
		
	# Printing out all scores and other class info
	def printScores(self,i):
		print("Player: " + self.name + " - Rolled " + str(i))
		print("Kept Di: " + str(self.keptDi))
		print("Rolled Di: " + str(self.rolledDi))
		print("--> 1 (#1s) - " + str(self.oneScore))
		print("--> 2 (#2s) - " + str(self.twoScore))
		print("--> 3 (#3s) - " + str(self.threeScore))
		print("--> 4 (#4s) - " + str(self.fourScore))
		print("--> 5 (#5s) - " + str(self.fiveScore))
		print("--> 6 (#6s) - " + str(self.sixScore))
		print("--> B (35) - " + str(self.bonusScore))
		print("--> T (3 x trips + other di) - " + str(self.tripleScore))
		print("--> Q (4 x quads + other di)- " + str(self.quadScore))
		print("--> F (25) - " + str(self.fullHouseScore))
		print("--> S (30) - " + str(self.shortScore))
		print("--> L (40) - " + str(self.longScore))
		print("--> Y (50) - " + str(self.yatziScore))
		print("--> C (ALL DI VALUE) - " + str(self.chanceScore))
		print("--> Total - " + str(self.totalScore))
			
		
	# Passing a list of integers of rolled dice and a single integer to keep
	def keepDi(self,  toKeep):
		if toKeep in self.rolledDi:
			self.keptDi.append(toKeep)
			self.rolledDi.remove(toKeep)
			self.amountOdDi = self.amountOdDi - 1
		else:
			print(str(toKeep) + " not in rolled list.")
			
	# Getting a value from the kept di list and removing from there
	def getDi(self, toGet):
		if toGet in self.keptDi:
			self.keptDi.remove(toGet)
			self.rolledDi.append(toGet)
			self.amountOdDi = self.amountOdDi + 1
		else:
			print(str(toGet) + " not in kept list.")
			
	# Resets kept di at end of turn
	def resetKeptDi(self):
		self.keptDi = []
		self.rolledDi = []
		self.amountOdDi = 5
		
	# Calculates the score of dice value selected	
	def calculateNumberScore(self,inputString):
		n = int(inputString)
		count = self.keptDi.count(n)
		ret = 1
		
		if n == 1 and self.oneScore == None:
			self.oneScore = count*1;
		elif n == 2 and self.twoScore == None:
			self.twoScore = count*2;
		elif n == 3 and self.threeScore == None:
			self.threeScore = count*3;
		elif n == 4 and self.fourScore == None:
			self.fourScore = count*4;
		elif n == 5 and self.fiveScore == None:
			self.fiveScore = count*5;
		elif n == 6 and self.sixScore == None:
			self.sixScore = count*6;
		else:
			print("Invalid input.")
			ret = 0
		return ret
		
	# Calculates the score of the di for chosen 3 of a kind or 4 of a kind
	def calculateTQScore(self,tq):
		if tq in(3,4):
			score = 0
			tripVal = 0
			ls = self.keptDi
			
			# Check to see if we can add a triple or quad score
			if (tq == 3 and self.tripleScore == None) or (tq == 4 and self.quadScore == None):
				
				# Looping through di values and counting
				for i in range(6):
					count = ls.count(i+1)
					if count >= tq:
						tripVal = i+1
						score = tripVal*count
						i = 7
						while tripVal in ls:
							ls.remove(tripVal)
						for k in ls:
							score = score + k
				if tq == 3:
					self.tripleScore = score
				elif tq == 4:
					self.quadScore = score
			else:
				print("Invalid input.")

# ----- Rolling Dice Methods -----		
# Returns a random integer
def roll_one_dice():
	return random.randrange(1,7) # Retruns random int from 1 (inclusive) to 7 (exclusive)

# Returns a list of n random integers
def roll_n_dice(n):
	ls = []
	for i in range(n):
		ls.append(roll_one_dice())
	return ls


# ----- Start of yatzi.py -----

player1 = player("Lukas",None,None,None,None,None,None,None,None,None,None,None,None,None,[],[])	
	

loop = True

while loop:
	i = 0
	while i < 4:		
		player1.printScores(i)
		print("--- Commands ---")
		print("--> Kn - keep value n")
		print("--> Gn - get value n")
		print("--> R - roll dice")
		print("--> E - end turn")
		print("--> X - exit")
		
		playerInput = input("What would you like to do? ")
		
		if playerInput in ("R","r"):
			print("ROLLING...")
			player1.rolledDi = roll_n_dice(player1.amountOdDi)
		elif playerInput in  ("E","e"):
			print("ENDING TURN")
			i = 4
		elif playerInput[0] in ("K","k"):
			print("KEEPING " + playerInput[1])
			player1.keepDi(int(playerInput[1]))
			i = i - 1
		elif playerInput[0] in ("G","g"):
			player1.getDi(int(playerInput[1]))
			i = i - 1
		elif playerInput in ("X","x"):
			i = 4
			loop = False
		elif playerInput in ("1","2","3","4","5","6"):
			if player1.calculateNumberScore(playerInput) == 1:
				i = 4
			else:
				i = i - 1
		elif playerInput in ("T","t"):
			player1.calculateTQScore(3)
			i = 4
		elif playerInput in ("Q","q"):
			player1.calculateTQScore(4)
			i = 4
		elif playerInput in ("F","f"):
			i = 4
		elif playerInput in ("S","s"):
			i = 4	
		elif playerInput in ("L","l"):
			i = 4
		elif playerInput in ("Y","y"):
			i = 4
		elif playerInput in ("C","c"):
			i = 4
		else:
			print("Invalid input.")
			i = i - 1
		
		i = i + 1
	player1.resetKeptDi()
	
		





