# Stone, Paper, Sizer Game
print("Stone, Paper, Sizer Game")
import random

number_of_guesses=1
var1=["Stone", "Paper", "Scissor"]
print("Number of Guesses is limited to 10 times only")
while (number_of_guesses<=10):
    var2 = random.choice(var1)
    var3=str(input("Please pick any of these three letters St:Stone, P:Paper, S:Scissor : "))
    if var3 == "St" and var2 == "Stone":
        print("You Won Play Again")
    elif var3 == "P" and var2 == "Scissor":
        print("You Won Play Again")
    elif var3 == "S" and var2 == "Paper":
        print("You Won Play Again")
    else:
        print("You Lose Play Again")
        print(number_of_guesses, "no.of guesses you took to finish.")


    print(10 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>10):
    print("Game Over")

