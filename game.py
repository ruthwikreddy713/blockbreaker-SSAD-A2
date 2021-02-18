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
				ball.move()	
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
			if(ball.collisionwithpaddle()==False):
				ballmov=False
			else:
				for brick in bricks:
					if(brick.strength!=0):
						if(brick.collisionwithball()==True):
							brick.strength=brick.strength-1
							brick.printbricks()
							if(brick.strength==0):
								brick.brokenbrick()
							elif(brick.strength>0 and brick.strength<=2):
								paddle.score=paddle.score+100
							break
				ball.move()
			start=time.time()
	printboard()