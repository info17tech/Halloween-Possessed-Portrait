import random
player=0
computer=0
s={1:'r',2:'p',3:'s'}
while True:
	comp=s[random.randint(1,3)]
	r=input("enter choice r/p/s")
	if(r=='r' and comp=='s') or (r=='p'and comp=='r') or (r=='s' and comp=='p'):
		print("you win")
		player=player+1
	else:
		print('comp wins')
		computer=computer+1
	if(player==3):
		print("Player is the winner")
		break
	elif(computer==3):
		print("Computer is the winner")
		break
	






