class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        
        def start(self):
            raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"

#Creating instances of Car and Motorcycle
    my_car = ("Toyota", "Camry", 2020)

#Using the start and stop methods without needing to know the internal implementaton
    print(my_car.start())
    print(my_car.stop())

#Code Explained
#_init_ is a special method in Python classes, also known as a constructor. 
#It is called when an object is created. 
#The self parameter refers to the instance of the class. 
#It is used to access variables that belong to the class. 
#The start method is an abstract method, which means it must be implemented by any subclass of Vehicle. 
#The Car class is a subclass of Vehicle and implements the start method. 
#The stop method is specific to the Car class. 
#We create an instance of the Car class and call the start and stop methods without needing to know the internal implementation of those methods. 
#This is an example of encapsulation, where the internal details of a class are hidden from the outside world.    