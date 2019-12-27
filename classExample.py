class Car:#Creates the Car class 
	color = "blue"#defines the color property of the car class
	mileage = 5000#defines the mileage property of the car class

Hyundai = Car()#creates an instance of the car class
print(Hyundai.color)#prints out the color property, of the car class object

class Jeep:#Creates the Jeep class
	def __init__(self,color,mileage):#defines the initial values of the Jeep class
		self.color = color#defines the initial color values as the value typed in the parameters of the object of the Jeep class
		self.mileage = mileage#defines the initial mileage values as the value typed in the parameters of the object of the Jeep class

Cherokee = Jeep("Tan",1000)#creates an object of the Jeep class with the jeep color and mileage in the parameters
print(Cherokee.color)#prints out the color property, of the jeep class object
