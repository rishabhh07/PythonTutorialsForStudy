# Oop14/Object oriented programming
# Operator Overloading & Dunder Methods
# My Practice
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

    def __add__(self, other): # __add__ dunder method
        return self.name + other.name

    def __iadd__(self, other):
        return self.score + other.score

    def __repr__(self):  # __repr dunder method
        return f"Score Card ({self.name}, {self.score}, {self.attempts})"

    def __str__(self):  # If __str__ is available on constructor then __str__ dunder will print by default.
                        # __repr will only print when we call it on print function
        return f"The name is {self.name}, Score is {self.score}, No. of attempts {self.attempts}"

Rishabh = Video_Game("Rishabh", 100, 1)
Sunny = Video_Game("Sunny", 99, 1)

print(Rishabh + Sunny)
print(repr(Rishabh))



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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))