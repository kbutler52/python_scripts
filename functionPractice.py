#Objective: create a function that prints all even numbers from 0-8 twice

def evenNumbers():#Creates a method
	for count in range(9):#Loops from 0 to 9
		if count % 2 == 0:#If count is even
			print(count)#print out count

evenNumbers()#calls the evenNumbers function
evenNumbers()#calls the evenNumbers function again
