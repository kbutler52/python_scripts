#The Purpose of this class is to create the Four_Math class
#The Four_Math class will:
#Add four to a number
#Subtract four from a number
#Multiply four to a number
#Divide four by a number

class Four_Math:
    def __init__(self,value):#Defines the default constructor for the Four_Math class
        self.number = value#Assigns the number attribute to value

    def AddFour(self):#Defines the AddFour function
        print("4 + "+str(self.number)+" = "+str(4+self.number))#Finds 4 + number and prints the result

    def SubFour(self):#Defines the SubFour function
        print("4 - " + str(self.number) + " = " + str(4 - self.number))  # Finds 4 - number and prints the result

    def MultFour(self):#Defines the MultFour function
        print("4 * " + str(self.number) + " = " + str(4 * self.number))  # Finds 4 * number and prints the result

    def DivFour(self):#Defines the DivFour function
        print("4 / " + str(self.number) + " = " + str(4 / self.number))  # Finds 4 / number and prints the result

#Comment out the next five lines when you are ready to work with imports

Test = Four_Math(2) #Makes an object of Four_Math class initializes the number value to 2
Test.AddFour()#Calls the AddFour() function in the Four_Math class
Test.SubFour()#Calls the SubFour() function in the Four_Math class
Test.MultFour()#Calls the MultFour() function in the Four_Math class
Test.DivFour()#Calls the DivFour() function in the Four_Math class