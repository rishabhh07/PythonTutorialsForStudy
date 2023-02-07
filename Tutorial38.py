# Oop3/Object oriented programming
# Self & __init__() (Constructors)
# My Practice

class Game:
    game = "BGMI"   #Class variables. You cannot change it from instancr variables.
    def __init__(self, name, score, attempts):
        self.name = name
        self.score = score
        self.attempts = attempts

    def Score_card(self):
        return f"The name is {self.name}, Score is {self.score}, No. of attempts {self.attempts}"

Rishabh = Game("Rishabh", 95, 7)
Priya = Game("Priya", 90, 9)

# Rishabh.name = "Rishabh" #Instance Vrriables
# Rishabh.score = 95    #Instance Vrriables
# Rishabh.attempts = 7   #Instance Vrriables
#
# Priya.name = "Priya"   #Instance Vrriables
# Priya.score = 90    #Instance Vrriables
# Priya.attempts = 9    #Instance Vrriables

print(Priya.score)
#
#
#
#
# # Decribed by harry
# # Self keyword:
# def read_number(self):
#     print(self.num)
#
#
# # Constructor in Python
# # __init__.
# def __init__(self):
#     # body of the constructor


# For Example:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
#     # Output: John




# Code as described/written in the video

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)

