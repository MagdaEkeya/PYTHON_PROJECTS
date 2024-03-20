#Abstraction from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    #Class, Object, Encapsulation
    class Circle(Shape):
        def __init__(self, radius):
            self.__radius = radius

        def area(self):
            return 3.14 * self.__radius * self.__radius

        def perimeter(self):
            return 2 * 3.14 * self.__radius
        
        #Inheritance 
        class Square(Shape):
            def __init__(self, side):
                self.__side = side

            def area(self):
                return self.__side * self.__side

            def perimeter(self):
                return 4 * self.__side
            
            #Polymorphism
            def print_area(self):
                print(f"The area of the shape is {self.area()}")

                #Creating objects and demostrate polymorphism
                circle = Circle(7)
                square = Square(4)
                print_area(circle) #Output: The area of the shape is 153.86
                print_area(square) #Output: The area of the shape is 16
                #Code Explained