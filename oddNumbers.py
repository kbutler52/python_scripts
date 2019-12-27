#Objective- print odd numbers 0-8 twice
# using the while loop


def oddNumbers():
	count=0
	while count<=8:
		if count % 2>0:
			print(count)
		
		count+=1

#oddNumbers()
#oddNumbers()


#Objective- print odd numbers 0-8 twice
#using the for loop

def oddNumbers1():
	for count in range(9):
		if count %2>0:
			print(count)

oddNumbers1()
oddNumbers1()

		
