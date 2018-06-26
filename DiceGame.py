# Assignment 4:  Build a program that simulates rounds of randomly rolling 2 six-sided dice.
# The program must keep track of the number of rounds, and check for and report when you roll a doubles.
#@author Anand Prasad
#@ Date 03/19/2018

import random

DICE_MIN = 1
DICE_MAX = 6

def diceOutCome():
	outCome = random.randrange(DICE_MIN, DICE_MAX + 1)
	return outCome

def Dice():
	#Main Code
	fDiceOC = diceOutCome()
	sDiceOC = diceOutCome()
	results = 'You have rolled a ' +  str(fDiceOC)  + ' and a '  +  str(sDiceOC)
	return  results


