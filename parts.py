import numpy as np
from random import randint
from board import *
board=np.zeros((120,40),dtype='U1')
for i in range(120):
	for j in range(40):
		board[i][j]=" "
class Paddle:
	def __init__(self,x,lent,lives,time):
		self.x=x
		self.lent=lent 
		self.lives=lives
		self.time=time
	def left(self):
		if(self.x>=1):
			self.x = self.x - 1
			for i in range(self.lent):
				board[self.x+i][39]="X"
			board[self.x+self.lent][39]=" "
	def right(self):
		if(self.x + self.lent< 118):
			self.x= self.x +1 
			for i in range(self.lent):
				board[self.x+i][39]="X"
			board[self.x-1][39]=" "
class Ball:
	def __init__(self,x,y):
		self.x=x
		self.y=y

paddle= Paddle(randint(0,113),7,3,0)
#board[10][10]="Y"
#print((board[10][10]),end="en")
for i in range(paddle.lent):
	board[paddle.x+i][39]="X"