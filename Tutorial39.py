# Oop4/Object oriented programming
# Class Methods In Python
# My Python
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

Rishabh = Game("Rishabh", 95, 7)
Priya = Game("Priya", 90, 9)
Rishabh.change_game("Counter Strike")
print(Priya.game)



class Movies:
    Favoirate_Movie = "Instreller"

    def __init__(self, name, Ganre):
        self.name = name
        self.Ganre = Ganre

    @classmethod
    def ChangeFavoirate_Movie(cls, New_Movie):
        cls.Favoirate_Movie = New_Movie

Shutter_Iseland = Movies("Shutter_Island", "Si-Fi")
Lala_land = Movies("Life", "RomCom")
Shutter_Iseland.ChangeFavoirate_Movie("ZNMD")
print(Lala_land.Favoirate_Movie)



# Decrived by Harry
class myClass:
    @classmethod
    def myfunc (cls, arg1, arg2, ...):
                          ...