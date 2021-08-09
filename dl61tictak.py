a= [1,2,3,4,5,6,7,8,9]
def printBoard():
	print(a[0],'|',a[1],'|',a[2])
	print("....................")
	print(a[3],'|',a[4],'|',a[5])
	print("....................")
	print(a[6],'|',a[7],'|',a[8])
	print("....................")

playeroneturn = True
while True:
	printBoard()
	p = int(input("choose your place, >>"))
	if(p in a):
			if playeroneturn:
				print("player1 chose:" , p)
				a[p-1] = 'x'
				playeroneturn = not playeroneturn
			else:
				print("player2 chose:" , p)
				a[p-1] = 'O'
				playeroneturn = not playeroneturn

			for i in (0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					if a[i]=='x':
						print("player 1 wins!")
						exit()
					else:
						print("player 2 wins!")
						exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					if a[i]=='x':
						print("player 1 wins!")
						exit()
					else:
						print("player 2 wins!")
						exit()
		
	else:
		continue
		
	if(a[0]==a[4] and a[0]==a[8]): 				
		printboard()
		if(a[0]=='X'):
				print("Player 1 wins")
				exit()
		else:
				print("Computer wins")
				exit()

	elif(a[2]==a[4] and a[2]==a[6]): 
		printboard()
		if(a[2]=='X'):
				print("Player 1 wins")
				exit()
		else:
				print("Computer wins")
				exit()
	t = possibilities()
	if len(t) == 0:
		printboard()
		print("It's a tie ...")
		exit()	 			


		


