# Oop5/Object oriented programming
# Class Methods As Alternative Constructors
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

    @classmethod                          #Class Methods As Alternative Constructors
    def devide_with_comma(cls,string):
        # rs = string.split(",")
        # return cls(rs[0],rs[1],rs[2])
        return cls(*string.split(","))

Rishabh = Game("Rishabh", 95, 7)
Priya = Game("Priya", 90, 9)
Sunny = Game.devide_with_comma("Sunny,95,8")
Rishabh.change_game("Counter Strike")
print(Sunny.attempts)
