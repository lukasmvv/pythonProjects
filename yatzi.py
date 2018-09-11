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
	def __init__(self, name, oneScore, twoScore, threeScore, fourScore, fiveScore, sixScore, tripleScore, quadScore, fullHouseScore, yatziScore, chanceScore, rolledDi, keptDi):
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
		print("--> 1 - " + str(self.oneScore))
		print("--> 2 - " + str(self.twoScore))
		print("--> 3 - " + str(self.threeScore))
		print("--> 4 - " + str(self.fourScore))
		print("--> 5 - " + str(self.fiveScore))
		print("--> 6 - " + str(self.sixScore))
		print("--> B - " + str(self.bonusScore))
		print("--> T - " + str(self.tripleScore))
		print("--> Q - " + str(self.quadScore))
		print("--> F - " + str(self.fullHouseScore))
		print("--> Y - " + str(self.yatziScore))
		print("--> C - " + str(self.chanceScore))
			
		
	# Passing a list of integers of rolled dice and a single integer to keep
	def keepDi(self,  toKeep):
		if toKeep in self.rolledDi:
			self.keptDi.append(toKeep)
			self.rolledDi.remove(toKeep)
			self.amountOdDi = self.amountOdDi - 1
		else:
			print(str(toKeep) + " not in rolled list")
			
	# Resets kept di at end of turn
	def resetKeptDi(self):
		self.keptDi = []
		self.rolledDi = []
		self.amountOdDi = 6


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
player1 = player("Lukas",0,0,0,0,0,0,0,0,0,0,0,[],[])	
	

loop = True

while loop:
	i = 0
	while i < 4:		
		player1.printScores(i)
		print("--- Commands ---")
		print("--> Kn - keep value n")
		print("--> R - roll dice")
		print("--> E - end turn")
		print("--> X - exit")
		
		playerInput = input("What would you like to do? ")
		
		if playerInput == "R":
			print("ROLLING...")
			player1.rolledDi = roll_n_dice(player1.amountOdDi)
		elif playerInput == "E":
			print("ENDING TURN")
			i = 4
		elif playerInput[0] == "K":
			print("KEEPING " + playerInput[1])
			player1.keepDi(int(playerInput[1]))
			i = i - 1
		elif playerInput == "X":
			i = 4
			loop = False
		
		i = i + 1
	player1.resetKeptDi()
	
		





