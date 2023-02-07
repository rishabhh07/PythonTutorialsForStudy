# Oop6/Object oriented programming
# Static Methods In Python
# My Practice
class Game:
    game = "BGMI"   #Class variables. You cannot change it from instancr variables.
    def __init__(self, name, score, attempts):
        self.name = name
        self.score = score
        self.attempts = attempts

    def Score_card(self):
        return f"The name is {self.name}, Score is {self.score}, No. of attempts {self.attempts}"

    @classmethod
    def change_game(cls, New_game):
        cls.game = New_game

    @staticmethod
    def print_my_name(string):
        print("This is my name : "+ string) # Static Methods


    @classmethod                          #Class Methods As Alternative Constructors
    def devide_with_comma(cls,string):
        # rs = string.split(",")
        # return cls(rs[0],rs[1],rs[2])
        return cls(*string.split(","))

Rishabh = Game("Rishabh", 95, 7)
Priya = Game("Priya", 90, 9)
Sunny = Game.devide_with_comma("Sunny,95,8")
Rishabh.change_game("Counter Strike")
print(Sunny.print_my_name("Rishabh"))



# Decribed by Harry
# In Python, static methods can be created using @staticmethod.
class Student:
@staticmethod
    def myfunc():
        //Code to be executed


# Alternatively, we can follow the below syntax as well:
# staticmethod(class_name.method())


# Code as described/written in the video

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")


