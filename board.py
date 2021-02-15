
import os
from parts import *
def printboard():
	os.system('clear')
	print("\n")
	print("\tLives : ",end=" ")
	print("\t\t",end=" ")
	print("Time : ",end=" ")
	print("\t\t",end="\n\n")
	for i in range(0, 120):
		print('\x1b[0;30;41m' + " " + '\x1b[0m', end="")
	print("")
	for i in range(0,40):
		print('\x1b[0;30;41m' + " " + '\x1b[0m', end="")
		for j in range(118):
			if(board[j][i]!=''):
				print('\x1b[0;30;36m' + str(board[j][i]) + '\x1b[0m', end="")
			else:
				print(" ", end="")
		print('\x1b[0;30;41m' + " " + '\x1b[0m', end="\n")
	for i in range(0, 120):
		print('\x1b[0;30;41m' + " " + '\x1b[0m', end="")
	print("")	
#printboard()