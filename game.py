from board import *
from parts import *
from input import *
from powerups import *
import sys,time
ballmov=False
start = time.time()
astart = time.time()
brokenbricks=0
bricks=level1bricks()
powerupss=[]
skip=0
bombs=[]
once=True
bombdrop=0
lostlife=0
while(True):
	inp = input_to(Get())
	current=time.time()
	if(current - astart > 1):
		paddle.time=paddle.time+1
		astart = time.time()
	if(inp=='s'):
		if(skip!=0):
			paddle.level=paddle.level+1
		skip=skip+1
	#print(bricks)
	if(paddle.lives==0 or paddle.time>500):
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
			"┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n",
			"You Lost\n")
		break
	elif((brokenbricks==len(bricks) and paddle.level==1) or skip==1 or (brokenbricks==len(bricks) and paddle.level==2)):
		skip=4
		ballmov=False
		brokenbricks=0
		for powerup in powerupss:
			if(powerup.active==2):	
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
			board[powerup.x][powerup.y]=""
		board[ball.px][ball.py]=""
		ball.prev="X"
		ball.newlevel()
		powerupss.clear()
		tempscore=paddle.score
		for brick in bricks:
			brick.brokenbrick()
		paddle.score=tempscore
		bricks.clear()
		paddle.level=paddle.level+1
		bricks=level2bricks()
	elif(paddle.level==3 and once):
		once=False
		ballmov=False
		for powerup in powerupss:
			if(powerup.active==2):	
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
			board[powerup.x][powerup.y]=""
		board[ball.px][ball.py]=""
		ball.prev="X"
		ball.newlevel()
		powerupss.clear()
		tempscore=paddle.score
		for brick in bricks:
			brick.brokenbrick()
		paddle.score=tempscore
		bricks.clear()
		ufo=UFO(paddle.x,4,9)
		ufo.initialise()
		bricks=level3bricks()
	elif(paddle.level==4):
		paddle.level=4
		print(" ___ _   _  ___ ___ ___  ___ ___ \n",
			"/ __| | | |/ __/ __/ _ \/ __/ __|\n",
			"\__ \ |_| | (_| (_|  __/\__ \__ \n",
			"|___/\__,_|\___\___\___||___/___/)\n")
		break				
	if (ballmov==False):
		if(inp=='a'):
			paddle.left()
			ball.moveunreleasedleft()
			if(paddle.level==3):
				ufo.moveleft()
		elif(inp=='d'):
			paddle.right()
			ball.moveunreleasedright()
			if(paddle.level==3):
				ufo.moveright()
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
			if(paddle.level==3):
				ufo.moveleft()
		elif(inp=='d'):
			paddle.right()
			if(paddle.level==3):
				ufo.moveright()
		elif(inp=='q'):
			break
	#current=time.time()
		if(current-start > 0.05):
			#ball.collisionwithframe()
			val=ball.collisionwithpaddle()
			if(val==0):
				ballmov=False
				for powerup in powerupss:
					if(powerup.active==2):	
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
					board[powerup.x][powerup.y]=""
				board[ball.px][ball.py]=""
				ball.prev="X"
				ball.newlife()
				powerupss.clear()
				if(paddle.level==3):
					ufo.removefromthatplace()
					ufo.x=paddle.x+1
					ufo.initialise()
			elif(val==1):
				for powerup in powerupss:
					if(powerup.name=="P" and powerup.active==4):
						ballmov=False
						powerup.active=3
			if(ballmov==True):
				if(paddle.level!=3):	
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
									if(paddle.level!=3):
										randnum=randint(1,100)
										'''if(brick.x <= 100 and randnum<=75):
											powerup=powerups(brick.x,brick.y,"",current,"P",1)
											powerupss.append(powerup)
											board[brick.x][brick.y]="P"'''									
										if(randnum<=20):
											powerup=powerups(brick.x,brick.y,"",current,"E",1)
											powerupss.append(powerup)
											board[brick.x][brick.y]="E"
										elif(randnum<=40):
											powerup=powerups(brick.x,brick.y,"",current,"S",1)
											powerupss.append(powerup)
											board[brick.x][brick.y]="S"
										elif(randnum<=60):
											powerup=powerups(brick.x,brick.y,"",current,"F",1)
											powerupss.append(powerup)
											board[brick.x][brick.y]="F"
										elif(randnum<=80):	
											powerup=powerups(brick.x,brick.y,"",current,"T",1)
											powerupss.append(powerup)
											board[brick.x][brick.y]="T"
										elif(randnum<=100):
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
				if(paddle.level==3):
					ufocoll=ufo.collisionwithball()
					if(ufocoll):
						if(ufo.strength!=0):
							ufo.strength=ufo.strength-1
						if(ufo.strength==6):
							tempbricks=UFObricks2()
							bricks+=tempbricks
							#print(len(bricks))
						if(ufo.strength==3):
							tempbricks=UFObricks1()
							bricks=tempbricks
						if(ufo.strength==0):
							paddle.level=paddle.level+1
					if(current-bombdrop>3):
						print("Hello")
						bombdrop=current
						bomb=Bomb(ufo.x,ufo.y+2,board[ufo.x][ufo.y+2])
						board[bomb.x][bomb.y]="B"
						bombs.append(bomb)
					for bomb in bombs:
						bomb.drop()
						if(bomb.collisionwithpaddle()==True):
							ballmov=False
							board[ball.px][ball.py]=""
							ball.prev="X"
							ball.newlife()
							ufo.removefromthatplace()
							ufo.x=paddle.x+1
							ufo.initialise()
							lostlife=1
					if(lostlife==1):
						lostlife=0
						for bomb in bombs:
							board[bomb.x][bomb.y]=""
						bombs.clear()
				ball.move()
				start=time.time()
	printboard()