# This program plays the classic Yatzi game
# Author: Lukas van Vuuren

import random

# ----- Player Class -----
class player:

	# Class variables
	toBonusScore = 0
	totalScore = 0
	bonusScore = 0
	amountOdDi = 5
	bottomScore = 0
	topScore = 0
	
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
		print("\tPlayer: " + self.name + " - Rolled " + str(i))
		print("\tKept Di: " + str(self.keptDi))
		print("\tRolled Di: " + str(self.rolledDi))
		print("\t--> 1 (#1s) - " + str(self.oneScore))
		print("\t--> 2 (#2s) - " + str(self.twoScore))
		print("\t--> 3 (#3s) - " + str(self.threeScore))
		print("\t--> 4 (#4s) - " + str(self.fourScore))
		print("\t--> 5 (#5s) - " + str(self.fiveScore))
		print("\t--> 6 (#6s) - " + str(self.sixScore))
		print("\t--> Top Score - " + str(self.toBonusScore))
		print("\t--> B (35) - " + str(self.bonusScore))
		print("\t--> Top Score - " + str(self.topScore))
		print("\t--> T (3 x trips + other di) - " + str(self.tripleScore))
		print("\t--> Q (4 x quads + other di)- " + str(self.quadScore))
		print("\t--> F (25) - " + str(self.fullHouseScore))
		print("\t--> S (30) - " + str(self.shortScore))
		print("\t--> L (40) - " + str(self.longScore))
		print("\t--> Y (50) - " + str(self.yatziScore))
		print("\t--> C (ALL DI VALUE) - " + str(self.chanceScore))
		print("\t--> Bottom Score - " + str(self.bottomScore))
		print("\t--> Total - " + str(self.totalScore))
			
		
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
			self.toBonusScore = self.toBonusScore + self.oneScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		elif n == 2 and self.twoScore == None:
			self.twoScore = count*2;
			self.toBonusScore = self.toBonusScore + self.twoScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		elif n == 3 and self.threeScore == None:
			self.threeScore = count*3;
			self.toBonusScore = self.toBonusScore + self.threeScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		elif n == 4 and self.fourScore == None:
			self.fourScore = count*4;
			self.toBonusScore = self.toBonusScore + self.fourScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		elif n == 5 and self.fiveScore == None:
			self.fiveScore = count*5;
			self.toBonusScore = self.toBonusScore + self.fiveScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		elif n == 6 and self.sixScore == None:
			self.sixScore = count*6;
			self.toBonusScore = self.toBonusScore + self.sixScore
			if self.toBonusScore >= 63:
				self.bonusScore = 35
		else:
			print("Invalid input.")
			ret = 0
		return ret
		
	# Calculates the score of the di for chosen 3 of a kind or 4 of a kind
	def calculateTQScore(self,tq):
		ret = 1
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
					self.bottomScore = self.bottomScore + self.tripleScore
				elif tq == 4:
					self.quadScore = score
					self.bottomScore = self.bottomScore + self.quadScore
			else:
				print("Invalid input.")
				ret = 0
		return ret
		
	# Calculates the full house score
	def calculateFullHouseScore(self):
		ret = 1
		score = 0
		if self.fullHouseScore == None:
			countThree = 0
			countTwo = 0
			ls = self.keptDi
			for i in range(6):
				if ls.count(i+1) == 2:
					countTwo = 1
				elif ls.count(i+1) == 3:
					countThree = 1
			if countTwo and countThree:
					score = 25
		else:
			ret = 0
		self.fullHouseScore = score
		self.bottomScore = self.bottomScore + self.fullHouseScore
		return ret
		
	# Calculates the short/long straight score given input
	def calculateStraightScore(self,n):
		ret = 1
		score = 0
		if (n == 4 and self.shortScore == None) or (n == 5 and self.longScore == None):
			ls = orderAndRemoveDups(self.keptDi)
			if len(ls) >= n:
				if n == 4:
					score = 30
				elif n == 5:
					score = 40
		else:
			ret = 0
		if n == 4 and self.shortScore == None:
			self.shortScore = score
			self.bottomScore = self.bottomScore + self.shortScore
		elif n == 5 and self.longScore == None:
			self.longScore = score
			self.bottomScore = self.bottomScore + self.longScore
		return ret
	
	# Calculates if there is yatzi in the kept di
	def calculateYatzi(self):
		ret = 1
		if self.yatziScore == None:
			ls = self.keptDi
			val = ls[0]			
			score = 0
			if ls.count(val) == 5:
				score = 50
			self.yatziScore = score
			self.bottomScore = self.bottomScore + self.yatziScore
				
		else:
			print("Invalid input.")
			ret = 0
		return ret
				
	# Calculates the sum of all di values
	def calculateChance(self):
		ret = 1
		if self.chanceScore == None:
			score = 0
			ls = self.keptDi
			for i in ls:
				score = score + i
			self.chanceScore = score
			self.bottomScore = self.bottomScore + self.chanceScore
		else:
			print("Invalid input.")
			ret = 0
		return ret

		
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
	
# ------ Ordering/Removing Methods ------
def orderAndRemoveDups(ls):
	return sorted(list(set(ls)))
	
	
# ------ Starting game -----
def startGame(players):	
	loop = True
	while loop:
		for p in players:
			for k in players:
				print(str(k.name) + " - " + str(k.totalScore))
			i = 0
			while i < 4:		
				p.printScores(i)
				print("--- Commands ---")
				print("--> Kn - keep value n")
				print("--> Gn - get value n")
				print("--> R - roll dice")
				print("--> X - exit")
				
				try:
					playerInput = input("What would you like to do? ")
				
					if playerInput in ("R","r"):
						if i == 3:
							print("Invalid input")
							i = i - 1
						else:
							print("ROLLING...")
							p.rolledDi = roll_n_dice(p.amountOdDi)
					elif playerInput[0] in ("K","k"):
						for c in playerInput:
							if c in ("1","2","3","4","5","6"):
								print("KEEPING " + c)
								p.keepDi(int(c))
						i = i - 1
					elif playerInput[0] in ("G","g"):
						for c in playerInput:
							if c in ("1","2","3","4","5","6"):
								p.getDi(int(c))
						i = i - 1
					elif playerInput in ("X","x"):
						return
					elif playerInput in ("1","2","3","4","5","6"):
						if p.calculateNumberScore(playerInput) == 1:
							i = 4
						else:
							i = i - 1
					elif playerInput in ("T","t"):
						if p.calculateTQScore(3) == 1:
							i = 4
						else:
							i = i - 1
					elif playerInput in ("Q","q"):
						if p.calculateTQScore(4) == 1:
							i = 4
						else: 
							i = i - 1
					elif playerInput in ("F","f"):
						if p.calculateFullHouseScore() == 1:
							i = 4
						else:
							i = i - 1
					elif playerInput in ("S","s"):
						if p.calculateStraightScore(4) == 1:
							i = 4
						else:
							i = i - 1	
					elif playerInput in ("L","l"):
						if p.calculateStraightScore(5) == 1:
							i = 4
						else:
							i = i - 1
					elif playerInput in ("Y","y"):
						if p.calculateYatzi() == 1:
							i = 4
						else:
							i = i - 1				
					elif playerInput in ("C","c"):
						if p.calculateChance() == 1:
							i = 4
						else:
							i = i - 1
					else:
						print("Invalid input.")
						i = i - 1
					
					i = i + 1
					p.topScore = p.toBonusScore + p.bonusScore
					p.totalScore = p.topScore + p.bottomScore
				except:
					print("Invalid input")
			p.resetKeptDi()


# ----- Start of yatzi.py -----

# Hard-coded list of players
players = []
player1 = player("Lukas",None,None,None,None,None,None,None,None,None,None,None,None,None,[],[])	
player2 = player("Leana",None,None,None,None,None,None,None,None,None,None,None,None,None,[],[])
players.append(player1)
players.append(player2)
	
# Starting game
startGame(players)

# Printing final scores
for p in players:
	print(str(p.name) + " - " + str(p.totalScore))
		





