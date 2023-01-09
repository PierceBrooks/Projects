# Pierce Brooks

# Speed Test Calc

# This program takes a car and coverts the speed of it based on different vairables


#this code is the class

class Car:
    __year=2000
    __make="ford"
    __model="explorer"
    __speed=0
    
    def setSpeed(self,speed):
        
        self.__speed=speed
        
    def setMake(self,make):
        
        self.__make=make
        
    def setModel(self,model):
        
        self.__model=model
        
    def setYear(self,year):
        
        self.__year=year
        
    def getSpeed(self):
        
        return self.__speed
    
    def getMake(self):
        
        return self.__make
    
    def getModel(self):
        
        return self.__model
    
    def getYear(self):
        
        return self.__year
    
    def accelerate(self):

       self.__speed += 5
       
       return self.__speed

    def brake(self):

       self.__speed -= 5
       
       return self.__speed

#This is the code that handles all three test with different variables lines 62-63

car = Car()
# car.setSpeed(100)
car.setSpeed(-5)
for i in range(1,6):

   limit=car.accelerate()

#Will not let speed go over 120
   
   if(limit>120):
       
       car.brake()
       
       print("Warning:you can not go faster than 120 MPH!")
       
       print("The speed of the car after the accelaration number ",i,"is :",car.getSpeed())
       
   else:
       
       print("The speed of the car after the accelaration number ",i,"is :",car.getSpeed())

for i in range(1,6):

   brake=car.brake()
   
   if(brake>=0):
       
       print("The speed of the car after the brake number ",i,"is :",car.getSpeed())
       
   else:
       
       print("Unable to brake,the vehicle is not moving!!")
       
       car.accelerate()
       
       print("The speed of the car after the brake number ",i,"is :",car.getSpeed())
