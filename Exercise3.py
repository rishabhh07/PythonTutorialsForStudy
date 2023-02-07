#print("Guess the number")
#n=18
#while(True):


n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")














n=18
guess=1
while(guess<=9):
    inp=int(input("Guess the number :\n "))
    if inp<18:
        print("You've entered lesser number",inp)
    elif inp>18:
        print("You've entered higher number" ,inp)
    else:
        print("You Won")
        print("No. of guesses you took to finish",guess)
        break
    print("Number of chances left",9-guess)
    guess=guess+1

if guess>9:
    print("GAME OVER")


