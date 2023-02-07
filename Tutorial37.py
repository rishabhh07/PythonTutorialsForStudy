# Oop2/Object oriented programming
# Instance & Class Variables
# My Practice
class Game:
    game = "BGMI"   #Class variables. You cannot change itfrom instancr variables.
    pass

Rishabh = Game()
Priya = Game()

Rishabh.name = "Rishabh" #Instance Vrriables
Rishabh.score = 95    #Instance Vrriables
Rishabh.attempts = 7   #Instance Vrriables

Priya.name = "Rishabh"   #Instance Vrriables
Priya.score = 90    #Instance Vrriables
Priya.attempts = 9    #Instance Vrriables

print(Rishabh.game)


# Decribed by Harry
object.__dict__



# Code as described/written in the video
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

