from board import *
from parts import *
from input import *
from powerups import *
import sys,time
ballmov=False
start = time.time()
astart = time.time()
brokenbricks=0
powerupss=[]
while(True):
	current=time.time()
	if(current - astart > 1):
		paddle.time=paddle.time+1
		astart = time.time()
	if(paddle.lives==0 or brokenbricks==len(bricks) or paddle.time>500):
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
			val=ball.collisionwithpaddle()
			if(val==0):
				ballmov=False
				for powerup in powerupss:
					board[powerup.x][powerup.y]=""
				board[ball.px][ball.py]=0
				ball.prev="X"
				ball.newlife()
				powerupss.clear()
			elif(val==1):
				for powerup in powerupss:
					if(powerup.name=="P" and powerup.active==4):
						ballmov=False
						powerup.active=3
			if(ballmov==True):
				for powerup in powerupss:
					if(powerup.active==1):
						powerup.move()
						if(powerup.collisionwithpaddle()==True):
							if(powerup.name=='S'):
								shrinkpaddle.activate(powerup)
							elif(powerup.name=='F'):
								fastball.activate(powerup)
							elif(powerup.name=='E'):
								expandpaddle.activate(powerup)
							elif(powerup.name=='T'):
								passthrough.activate(powerup)
							elif(powerup.name=='P'):
								paddlegrab.activate(powerup)							
							powerup.active=2
							if(powerup.name=='P'):
								powerup.active=4
						elif(powerup.y==39):
							board[powerup.x][powerup.y]=""
					elif(current-powerup.time>20 and powerup.active==2):
						if(powerup.name=='S'):
							shrinkpaddle.deactivate(powerup)
						elif(powerup.name=='F'):
							fastball.deactivate(powerup)
						elif(powerup.name=='E'):
							expandpaddle.deactivate(powerup)
						elif(powerup.name=='T'):
							passthrough.deactivate(powerup)
						elif(powerup.name=='P'):
							paddlegrab.deactivate(powerup)						
						powerup.active=3
				for brick in bricks:
					if(brick.strength!=0):
						prevx=ball.vx
						prevy=ball.vy
						if(brick.collisionwithball()==True):
							if(ball.passthrough==0):
								brick.strength=brick.strength-1
								brick.printbricks()
								if(brick.strength==0):
									brick.brokenbrick()
									brokenbricks=brokenbricks+1
									randnum=randint(1,100)
									'''if(brick.x <= 100 and randnum<=75):
										powerup=powerups(brick.x,brick.y,"",current,"P",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="P"'''									
									if(randnum<=15):
										powerup=powerups(brick.x,brick.y,"",current,"E",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="E"
									elif(randnum<=30):
										powerup=powerups(brick.x,brick.y,"",current,"S",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="S"
									elif(randnum<=45):
										powerup=powerups(brick.x,brick.y,"",current,"F",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="F"
									elif(randnum<=60):	
										powerup=powerups(brick.x,brick.y,"",current,"T",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="T"
									elif(randnum<=75):
										powerup=powerups(brick.x,brick.y,"",current,"P",1)
										powerupss.append(powerup)
										board[brick.x][brick.y]="P"
								elif(brick.strength>0 and brick.strength<=2):
									paddle.score=paddle.score+100
								break
							else:
								brick.brokenbrick()
								ball.vx=prevx
								ball.vy=prevy
								brick.strength=0
								brokenbricks=brokenbricks+1
				ball.move()
				start=time.time()
	printboard()