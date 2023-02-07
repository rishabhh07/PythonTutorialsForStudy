# Oop7/Object oriented programming
# Single Inheritance
# My Practice

# Parent Class
class Video_Game:
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

# Single Inheritance
# Child Class
class Outdoor_game(Video_Game):
    def __init__(self, name, score, attempts, sixes, fours):
        self.name = name
        self.score = score
        self.attempts = attempts
        self.sixes = sixes
        self.fours = fours


    def Score_Board(self):
        return f"The name is {self.name}, Score is {self.score}, No. of attempts {self.attempts}, " \
               f"No.of Fours {self.sixes}, No.of Fours {self.fours}"

Rishabh = Video_Game("Rishabh", 95, 7)
Priya = Video_Game("Priya", 90, 9)
Sunny = Video_Game.devide_with_comma("Sunny,95,8")
Rishabh.change_game("Counter Strike")
Dhoni = Outdoor_game("Dhoni", 100, 5, 101, 98)
Virat = Outdoor_game("Virat", 122, 3, 75, 150)
print(Sunny.print_my_name("Rishabh"))
print(Virat.Score_Board())



# Decribed by Harry
"""Inheritance is the ability to define a new class(child class) 
that is a modified version of an existing class(parent class)"""
# Syntax:
# class Parent_class_Name:
#Parent_class code block
# class Child_class_Name(Parent_class_name):
#Child_class code block


# Different forms of Inheritance:
# 1. Single inheritance:
# When a child class inherits from only one parent class then it is called single inheritance.
# 2. Multiple inheritance:
# When a child class inherits from multiple parent classes then it is called multiple inheritance.

# Below is an example of single inheritance in Python.
class Parent():
    def first(self):
        print('Parent function')


class Child(Parent):
    def second(self):
        print('Child function')


object1 = Child()
object1.first()
object1.second()
# Output:
# Parent function
# Child function


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


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)

