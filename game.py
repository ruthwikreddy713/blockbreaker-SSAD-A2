from board import *
from parts import *
from input import *
import sys,time
ballmov=False
while(True):
	inp = input_to(Get())
	if(inp=='a'):
		paddle.left()
	elif(inp=='d'):
		paddle.right()
	elif(inp == ' ' and ballmov==False):
		if(ball.release()==True):
			prevx=ball.px
			prevy=ball.py
			ballmov=True
			board[prevx][prevy]="X"
	elif(inp=='q'):
		break
	if(ballmov==True):
		ball.collisionwithframe()
		ball.move()
	printboard()