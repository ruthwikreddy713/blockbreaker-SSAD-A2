from board import *
from parts import *
from input import *
import sys,time
while(True):
	printboard()	
	inp = input_to(Get())
	if(inp=='a'):
		paddle.left()
	elif(inp=='d'):
		paddle.right()
	elif(inp=='q'):
		break