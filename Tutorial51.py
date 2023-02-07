# Oop15/Object oriented programming
# Abstract Base Class & @abstractmethod
# My Practice
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class rectangle(shape):
    Shape_Tpye = "Reactangle"
    Sides = 4
    def __init__(self):
        self.length = 98
        self.breadth = 69

    def print_area(self):
        return self.length * self.breadth

class square(shape):
    Shape_Type = "Square"
    Sides = 4
    Sides_Type = "All Sides Are Equal"
    def __init__(self):
        self.length = 56

    def print_area(self):
        return self.length * 4

rectangle_area = rectangle()
square_area = square()

print(rectangle_area.print_area())
print(square_area.print_area())


# Described by Harry
# It is important to remember that we can not make an object for an abstract class.
# Following is the syntax for defining an abstract method in an abstract class in Python:
from abc import ABC, abstractmethod
Class MyClass(ABC):
      @abstractmethod
      def mymethod(self):
            #empty body
            pass


"""To implement an abstract class, we have to import the abc module by using an import statement. 
Along with it, we have to import the abstract method too. 
If we are using a Python version older than 3.4, then we have to write:"""
# from abc import ABCMeta, abstractmethod

# Moreover, we have to pass ABCMeta into the class, which we are defining as abstract.
# Although if our version is newer, then we can import by the statement:
# from abc import ABC, abstractmethod


# Code as described/written in the video

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())