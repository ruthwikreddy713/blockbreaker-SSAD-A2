from board import *
from parts import *
from input import *
import sys,time
ballmov=False
start = time.time()
astart = time.time()
while(True):
	current=time.time()
	if(current - astart > 1):
		paddle.time=paddle.time+1
		astart = time.time()
	if(paddle.lives==0):
		print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n",
			"███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n",
			"██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n",
			"██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n",
			"██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n",
			"███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n",
			"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n",
			"███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n",
			"██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n",
			"██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n",
			"██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n",
			"███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n",
			"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n")
		break
	inp = input_to(Get())
	if (ballmov==False):
		if(inp=='a'):
			paddle.left()
			ball.moveunreleasedleft()
		elif(inp=='d'):
			paddle.right()
			ball.moveunreleasedright()
		elif(inp == ' ' and ballmov==False):
			if(ball.release()==True):
				prevx=ball.px
				prevy=ball.py
				ballmov=True
				board[prevx][prevy]="X"	
		elif(inp=='q'):
			break
	else:	
		if(inp=='a'):
			paddle.left()
		elif(inp=='d'):
			paddle.right()
		elif(inp=='q'):
			break
	#current=time.time()
		if(current-start > 0.05):
			#ball.collisionwithframe()
			if(ball.move()==False):
				ballmov=False
			start=time.time()
	printboard()