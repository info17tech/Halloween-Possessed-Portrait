import random
count=0
while(count<=100):
	n=input("enter r to roll the dice,q to quit:")
	if (n=='r'):
		g=random.randint(1,6)
		print("dice value",g)
		count=count+g
		print ("your score is ",count)
		if(count==8):
			count=37
			print ("snake bite")
		elif(count==13):
			count=34
			print ("you have climed a ladder")
		elif(count==40):
			count=68
			print("you have climed a ladder")
		elif(count==52):
			count=81
			print ("you have climed a ladder")
		elif(count==76):
			count=97
			print ("you have climed a ladder")
		elif(count==38):
			count=9
			print ("snake bite")
		elif(count==25):
			count=4
			print ("snake bite")
		elif(count==11):
			count=3
			print ("snake bite")
		elif(count==65):
			count=46
			print ("snake bite")
		elif(count==89):
			count=70
			print ("snake bite")
		elif(count==93):
			count=64
			print ("snake bite")
		elif(count==100):
			print ("you win")
else:
	break	