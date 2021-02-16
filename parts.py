import numpy as np
from random import randint
from board import *
board=np.zeros((120,40),dtype='U1')
for i in range(120):
	for j in range(40):
		board[i][j]=""
class Paddle:
	def __init__(self,x,lent,lives,time):
		self.x=x
		self.lent=lent 
		self.lives=lives
		self.time=time
	def left(self):
		if(self.x>=1):
			#self.x = self.x - 1
			for i in range(self.lent):
				temp= board[self.x+i][39]
				board[self.x+i][39]=board[self.x+i-1][39]
				board[self.x+i-1][39]=temp
				#board[self.x+i-1][39]="X"
			self.x= self.x-1 
			board[self.x+self.lent][39]=""
	def right(self):
		if(self.x + self.lent< 118):
			#self.x= self.x +1 
			for i in range(1,self.lent+1):
				temp=board[self.x][39]
				board[self.x][39]=board[self.x+i][39]
				board[self.x+i][39]=temp
				#swap(board[self.x+i][39],board[self.x][39])
			self.x= self.x +1 
			board[self.x-1][39]=""
paddle= Paddle(randint(0,113),7,3,0)
#board[10][10]="Y"
#print((board[10][10]),end="en")
for i in range(paddle.lent):
	board[paddle.x+i][39]="X"
class Ball:
	def __init__(self,px,py,vx,vy):
		self.px=px
		self.py=py
		self.vx=vx
		self.vy=vy
	def moveunreleasedleft(self):
		if (paddle.x >=1 and self.py==39):
			self.px = self.px -1 
			board[self.px][self.py]="*"
	def moveunreleasedright(self):
		if(paddle.x + paddle.lent< 118):
			self.px = self.px + 1
			board[self.px][self.py]="*"
	def move(self):
		if (self.px >= paddle.x and self.py == 39 and self.px <= paddle.x + paddle.lent): 
			board[self.px][self.py]="X"
		else:
			board[self.px][self.py]=""
		if self.px + self.vx < 118 and self.px + self.vx >=0 :
			self.px=self.px + self.vx
		else:
			self.vx = -self.vx
		if self.py + self.vy <=39 and self.py + self.vy >0:
			self.py = self.py + self.vy
		else:
			#self.py
			if(self.py + self.vy <=0):
				self.vy=-self.vy
			else:
				#New ball
				for i in range(paddle.lent):
					board[paddle.x+i][39]=""
				paddle.lives=paddle.lives-1
				paddle.x = randint(0,112)
				paddle.lent = 7
				for i in range(paddle.lent):
					board[paddle.x+i][39]="X"
				board[ball.px][ball.py]=""
				ball.px=randint(paddle.x,paddle.x + paddle.lent)
				ball.py=39
				ball.vx=0
				ball.vy=0
				board[ball.px][ball.py]="*"
				return False
		board[self.px][self.py]="*"
		return True
	def release(self):
		if (self.px >= paddle.x and self.py == 39 and self.px <= paddle.x + paddle.lent): 
			if (self.px > paddle.x + 2):
				self.vx= 3 - (self.px - (paddle.x + 2))
			elif (self.px == (paddle.x + 2)):
				self.vx=3
			else:
				self.vx = -3+((paddle.x + 2)-self.px)
			self.vy = -2
			return True
		else:
			return False
	'''def collisionwithframe(self):
		if (self.px<=0 or self.px>=119):
			self.vx= -self.vx
		if (self.py <= 0):
			self.vy= -self.vy'''
		#def collisionwithpaddle(self):
ball = Ball(randint(paddle.x,paddle.x + paddle.lent),39,0,0)
board[ball.px][ball.py]="*"