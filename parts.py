import numpy as np
from random import randint
from board import *
from colorama import *
init()
board=[]
for i in range(120):
	row=[]
	for j in range(40):
		row.append("")
	board.append(row)
class Paddle:
	def __init__(self,x,lent,lives,time,score):
		self.x=x
		self.lent=lent 
		self.lives=lives
		self.time=time
		self.score=score
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
paddle= Paddle(#randint(0,113)
	85,7,3,0,0)
#board[10][10]="Y"
#print((board[10][10]),end="en")
for i in range(paddle.lent):
	board[paddle.x+i][39]="X"
class Ball:
	def __init__(self,px,py,vx,vy,prev,passthrough):
		self.px=px
		self.py=py
		self.vx=vx
		self.vy=vy
		self.prev=prev
		self.passthrough=passthrough
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
			board[self.px][self.py]=self.prev
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
		self.prev=board[self.px][self.py]
		board[self.px][self.py]="*"
		return True
	def release(self):
		if (self.px >= paddle.x and self.py == 39 and self.px <= paddle.x + paddle.lent): 
			if (self.px > paddle.x + paddle.lent//2):
				self.vx= paddle.lent//2 - (self.px - (paddle.x + paddle.lent//2))
			elif (self.px == (paddle.x + paddle.lent//2)):
				self.vx=0
			else:
				self.vx = -paddle.lent//2+((paddle.x + paddle.lent//2)-self.px)
			self.vy = -1
			return True
		else:
			return False
	'''def collisionwithframe(self):
		if (self.px<=0 or self.px>=119):
			self.vx= -self.vx
		if (self.py <= 0):
			self.vy= -self.vy'''
	def collisionwithpaddle(self):
		if self.py==39 and self.px >= paddle.x and self.px <= paddle.x + paddle.lent:
			self.vy = -self.vy
			if (self.px > paddle.x + (paddle.lent)//2):
				self.vx = 1+self.vx + paddle.lent//2 - (paddle.x+paddle.lent - self.px)
				#paddle.score=self.vx
			else:
				self.vx = self.vx - (paddle.x + (paddle.lent//2)-self.px)
				#paddle.score=self.vx
			return 1
		elif self.py==39:
			return 0
		return 2
	def newlife(self):
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
		ball.passthrough=0
		board[ball.px][ball.py]="*"
ball = Ball(#randint(paddle.x,paddle.x + paddle.lent)
	paddle.x+paddle.lent - 1,39,0,0,"",0)
board[ball.px][ball.py]="*"
class Bricks:
	def __init__ (self,x,y,strength):
		self.strength=strength
		self.x=x
		self.y=y
	def collisionwithball(self):
		#print(self.y,self.x,ball.px,ball.py)
		if ball.py >= self.y -2  and ball.py < self.y+1 and ball.vy>0:
			#print(self.x,self.y,ball.py,ball.px)
			if(ball.px < self.x - 1 and ball.vx > 0) or (ball.px > self.x + 1 and ball.vx < 0):
				if(ball.px + ball.vx >= self.x - 1 and ball.vx>0) or (ball.px + ball.vx <= self.x + 1 and ball.vx <0):
					if(ball.py+ball.vy == self.y -1 or ball.py+ball.vy==self.y + 1):
						#print("check\ncheck\ncheck\n")
						if(ball.px + ball.vx == self.x - 1 and ball.vx > 0) or(ball.px + ball.vx == self.x + 1 and ball.vx<0):
							#ball.px = ball.px+ball.vx
							if(ball.py+ball.vy==self.y-1):  #collision at posn 1,3
								#print("Coll at 1,3")
								ball.vy= -ball.vy
								return True
							elif(ball.py+ball.vy==self.y+1):   #collision at posn7
								#print("Coll at 7", self.x, self.y)
								ball.vx = -ball.vx
								return True
						elif(ball.py+ball.vy == self.y - 1): #collision at posn 2
							#print("Coll at 2")
							board[ball.px][ball.py]=ball.prev
							ball.px = self.x
							ball.vy = -ball.vy
							return True
						else:
							ball.vx=-ball.vx
							return True
					else:
						#print("Horizontal change")
						#board[ball.px][ball.py]=ball.prev
						#ball.move()
						ball.vx = - ball.vx
						return True
			if(ball.vx==0 and ball.px >= self.x-1 and ball.px <=self.x+1 and ball.py+ball.vy == self.y -1):
				#print("How")
				ball.vy=-ball.vy
				return True
			if(ball.px >= self.x -1 and ball.px <=self.x+1 and ball.py <=self.y+1 and ball.py <= self.y -1):
				if(ball.py==self.y):
					ball.vx=-ball.vx
				else:
					ball.vy=-ball.vy
				return True
		if ball.py >= self.y -1 and ball.py <= self.y +2 and ball.vy<0:
			#print("ok ",self.y,self.x,ball.px,ball.py)
			#print(self.y,self.x,ball.px,ball.py)
			if(ball.px < self.x - 1 and ball.vx > 0) or (ball.px > self.x + 1 and ball.vx < 0):
				if(ball.px + ball.vx >= self.x - 1 and ball.vx>0) or (ball.px + ball.vx <= self.x + 1 and ball.vx <0):
					if(ball.py+ball.vy == self.y -1 or ball.py+ball.vy==self.y + 1):
						#print("check\ncheck\ncheck\n")
						if(ball.px + ball.vx == self.x - 1 and ball.vx > 0) or(ball.px + ball.vx == self.x + 1 and ball.vx<0):
							#ball.px = ball.px+ball.vx
							if(ball.py+ball.vy==self.y+1):  #collision at posn 1,3
								#print("Coll at 1,3")
								ball.vy= -ball.vy
								return True
							elif(ball.py+ball.vy==self.y-1):   #collision at posn7
								#print("Coll at 7", self.x, self.y)
								ball.vx = -ball.vx
								return True
						elif(ball.py+ball.vy == self.y + 1): #collision at posn 2
							#print("Coll at 2")
							#board[ball.px][ball.py]=ball.prev
							#ball.px = self.x
							ball.vy = -ball.vy
							return True
						else:
							ball.vx=-ball.vx
							return True
					else:
						#print("Horizontal change")
						#board[ball.px][ball.py]=ball.prev
						#ball.move()
						ball.vx = - ball.vx
						return True
			if(ball.vx==0 and ball.px >= self.x-1 and ball.px <=self.x+1 and ball.py+ball.vy == self.y +1):
				#print("How")
				ball.vy=-ball.vy
				return True
			if(ball.px >= self.x -1 and ball.px <=self.x+1 and ball.py <=self.y+1 and ball.py >= self.y -1):
				if(ball.py==self.y):
					ball.vx=-ball.vx
				else:
					ball.vy=-ball.vy
				return True
		return False
	def brokenbrick(self):
		paddle.score=paddle.score+100
		board[self.x][self.y]=""
		board[self.x+1][self.y]=""
		board[self.x-1][self.y]=""
		board[self.x][self.y+1]=""
		board[self.x+1][self.y+1]=""
		board[self.x-1][self.y+1]=""
		board[self.x][self.y-1]=""
		board[self.x+1][self.y-1]=""
		board[self.x-1][self.y-1]=""
	def printbricks(self):
		if(self.strength==1):
			board[self.x+1][self.y]="|"
			board[self.x][self.y]=" "
			board[self.x-1][self.y]="|"
			for j in range(3):
				board[self.x -1 +j][self.y-1]="$"
				board[self.x -1 +j][self.y+1]="$"
		if(self.strength==2):
			board[self.x+1][self.y]=Fore.MAGENTA + "|"
			board[self.x][self.y]=Fore.MAGENTA + " "
			board[self.x-1][self.y]=Fore.MAGENTA + "|"
			for j in range(3):
				board[self.x -1 +j][self.y-1]=Fore.MAGENTA + "$"
				board[self.x -1 +j][self.y+1]=Fore.MAGENTA + "$"			

class Unbreakablebrick(Bricks):
	pass
	'''def __init__(self):
		Bricks.__init__(self)
		Bricks.strength=-1'''
bricks=[]
for i in range(15):
	brick=Bricks(12+6*i,7,2)
	board[11+6*i][7]= Fore.MAGENTA + "|"
	board[12+6*i][7]= Fore.MAGENTA + " "
	board[13+(6*i)][7]=Fore.MAGENTA + "|"
	for j in range(3):
		board[11+(6*i)+j][6]=Fore.MAGENTA + "$"
		board[11+(6*i)+j][8]=Fore.MAGENTA + "$"
	bricks.append(brick)
#bricks2=[]
for i in range(15):
	if(i%4==0):
		brick=Unbreakablebrick(21+6*i,11,-1)
		board[20+6*i][11]=Fore.RED + "|"
		board[21+6*i][11]=Fore.RED + " "
		board[22+(6*i)][11]=Fore.RED + "|"
		for j in range(3):
			board[20+(6*i)+j][10]=Fore.RED + "$"
			board[20+(6*i)+j][12]=Fore.RED + "$"	
		bricks.append(brick)
	elif(i%4==3):
		brick=Bricks(21+6*i,11,3)
		board[20+6*i][11]=Fore.GREEN + "|"
		board[21+6*i][11]=Fore.GREEN + " "
		board[22+(6*i)][11]=Fore.GREEN + "|"
		for j in range(3):
			board[20+(6*i)+j][10]=Fore.GREEN + "$"
			board[20+(6*i)+j][12]=Fore.GREEN + "$"	
		bricks.append(brick)
	else:
		brick=Bricks(21+6*i,11,1)
		board[20+6*i][11]= "|"
		board[21+6*i][11]= " "
		board[22+(6*i)][11]= "|"
		for j in range(3):
			board[20+(6*i)+j][10]="$"
			board[20+(6*i)+j][12]="$"
		bricks.append(brick)