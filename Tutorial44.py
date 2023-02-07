# Oop8/Object oriented programming
# Multiple Inheritance
# My Practice
class Video_Game:
    game = "BGMI"   #Class variables. You cannot change it from instancr variables.
    def __init__(self, name, score, attempts):
        self.name = name
        self.score = score
        self.attempts = attempts

    def Score_card(self):
        return f"The name is {self.name}, Score is {self.score}, No. of attempts {self.attempts}"

class Tournament:
    khel = "Cricket"
    def __init__(self, teams, captains):
        self.teams = teams
        self.captains = captains

    def team_details(self):
        return f"Team names {self.teams}, Captains are {self.captains}"

class AwesomePlayer(Video_Game, Tournament):
    def __init__(self, name, game):
        self.name = name
        self.game = game



Rishabh = Video_Game("Rishabh", 95, 7)
Priya = Video_Game("Priya", 90, 9)
Ipl = Tournament(["RCB", "CSK", "MI", "DC"], ["Virat Kohli", "MS Dhoni", "Rohit Sharma", "Shrayash Iyer"])
Virat = AwesomePlayer("Virat Kohli", "Cricket")
Dhoni = AwesomePlayer("MS Dhoni", "Cricket")


print(Ipl.teams)



# Decribed by Harry
class Base1:
    def func1(self):
        print("this is Base1 class")


class Base2:
    def func2(self):
        print("this is Base2 class")


class Child(Base1, Base2):
    def func3(self):
        print("this is Base3 class")


obj = Child()
obj.func1()
obj.func2()
obj.func3()

# Output:
# this is Base1 class
# this is Base2 class
# this is Base3 class



# Code as described/written in the video

class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
print(karan.var)

