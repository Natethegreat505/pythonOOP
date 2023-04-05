# Car class for demonstrating object oriented programming

# definition of the class, important that the class and the filename are the same
class Car:
    
    # We use the init function to define the attributes of the class, 
    # __init__ is shaped like a function because it is a function, one that is called when we "instantiate" the object.
    def __init__(self, year, make, speed):
        # The following attributes will be defined when the object is first created
        self.__year_model = year      # This holds the year of the car
        self.__make = make      # This holds the make of the car
        self.__speed = 0    # Initial speed is zero
    

    # Function: used to set the year model of the car object. The user's input here is "year"
    def set_year_model(self, year):
        self.__year_model = year

    # Function: used to set the make of the car. The user's input here is "make"
    def set_make(self, make):
        self.__make = make

    # Function: used to set the speed of the car. The user's input here is "speed"
    def set_speed(self, speed):
        self.__speed = speed

    # Function: retrieves data from the model_year attribute
    def get_model_year(self):
        return self.__year_model    # Returns the year model
    
    # Function: retrieves data from the make attribute
    def get_make(self):
        return self.__make      # Returns the make of the car

    # Function: retrieves the speed of the car
    def get_speed(self):
        return self.__speed     # Returns the speed of the car

    # Function: increase the speed of the car
    def accelerate(self):
        self.speed +=5

    # Function: decrease the speed of the car
    def brake(self):
        self.speed -=5
    



# Using the power of object oriented programming
# Instantiate the Car object and name it "mycar"
mycar = Car(2010, 'Mazda', 0)

# Lets set the speed
mycar.set_speed(20)

# Get the speed, convert it to a string, and print it within a descriptive string
print("Currently, my car speed is " + str(mycar.get_speed()) + " MPH")
