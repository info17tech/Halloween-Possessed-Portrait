import random
while True:
	n=(input("enter r to roll the dice,q to quit:"))
	
	if (n=='r'):
		g=random.randint(1,6)
		print(g)
	else:
         break