# Oop12/Object oriented programming
# Super() and Overriding In Classes
# My Practice
class A:
    var1 = "Rishabh"
    def __init__(self):
        self.var2 = "Sunny1"
        self.var3 = "Rohan1"
        self.Special = "Special"

class B(A):
    var2 = "Sunny"
    def __init__(self):
        # super().__init__() If we put "super" here then it search the variable in B class constructor then it will go to the A class constructor.
        self.var2 = "Sunny2"
        self.var3 = "Rohan2"
        super(B, self).__init__() # If we put "super" here then it will directly go to the A class constructor.
        print(super().var1) # First it prints the class variable of class A the it jumps into the constructor of class A.


a = A()
b = B()

print(b.var3)
# Super helps to jump on to the parent class/super class
# Super it helps to access the attributes or method of older class or parent class.




# Described by Harry
# Where does super() fit in all this?
class Parent_Class(object):
    def __init__(self):
        pass


class Child_Class(Parent_Class):
    def __init__(self):
        super().__init__()




# Code as described/written in the video:
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
