# Oop10/Object oriented programming
# Public, Private & Protected Access Specifiers
# My Practice

class Video_Game:
    game = "BGMI"      #Public Variable            #Class variables. You cannot change it from instancr variables.
    _game1 = "Contra"  #Protected Variable. We can only use this in child class.
    __game2 = "Super Mario"  #Private  Variable. We can only use this in this perticular class

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

Rishabh = Video_Game("Rishabh", 98, 2)
print(Rishabh.game)
print(Rishabh._game1)
print(Rishabh._Video_Game__game2)   #Name Mangling. We use this to access the private veriable (_classname__private vaiable)


# Described by Harry
# Example of public access modifier:
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age



# Example of protected access modifier:
class employee:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age  # protected attribute



# Example of private access modifier:
class employee:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age  # private attribute



# Code as described/written in the video

# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

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

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)
