import time
from parts import *
class powerups:
	def __init__(self,x,y,prev,time,name,active):
		self.x=x
		self.y=y
		self.prev=prev
		self.time=time
		self.active=active
		self.name=name
	def move(self):
		if(self.y <= 38):
			board[self.x][self.y]=self.prev
			self.y = self.y+1
			board[self.x][self.y]=self.name
		else:
			self.active=False
	def collisionwithpaddle(self):
		if self.y==39 and self.x >= paddle.x and self.x < paddle.x + paddle.lent:
			board[self.x][self.y]="X"
			return True
		return False
	def activate(self):
		self.active=2
	def deactivate(self):
		self.active=3
class expandpaddle(powerups):
	def activate(self):
		self.time=time.time()
		board[paddle.x-1][39]="X"
		board[paddle.x+paddle.lent][39]="X"		
		paddle.lent = paddle.lent + 2
		paddle.x=paddle.x-1
	def deactivate(self):
		board[paddle.x][39]=""
		board[paddle.x + paddle.lent - 1][39]=""
		paddle.lent = paddle.lent - 2
		paddle.x=paddle.x+1
class shrinkpaddle(powerups):
	def activate(self):
		if(paddle.lent>2):
			self.time=time.time()
			board[paddle.x][39]=""
			board[paddle.x + paddle.lent - 1][39]=""
			paddle.lent = paddle.lent - 2
			paddle.x=paddle.x+1
	def deactivate(self):
		board[paddle.x-1][39]="X"
		board[paddle.x+paddle.lent][39]="X"		
		paddle.lent = paddle.lent + 2
		paddle.x=paddle.x-1
class fastball(powerups):
	def activate(self):
		self.time=time.time()
		if(ball.vx>0):
			ball.vx=ball.vx + 2
		else:
			ball.vx=ball.vx -2
	def deactivate(self):
		if(ball.vx<=0):
			ball.vx=ball.vx + 2
		else:
			ball.vx=ball.vx -2
class passthrough(powerups):
	def activate(self):
		self.time=time.time()
		ball.passthrough=ball.passthrough+1
		#self.active=2
	def deactivate(self):
		ball.passthrough=ball.passthrough-1
class paddlegrab(powerups):
	pass
		#self.active=3
#class throughball(powerups):
#	def activate(self):
