# print("Health Management System")
print("Welcome to the Health Management System")

def get_date_time():
    import datetime
    return datetime.datetime.now()


# 1 for Anuj , 2 for Devanshu ,  3 for Massive
print("Enter the member unique id for which you want to update diet or exercise")
input_1 = int(input())
if input_1 not in [1,2,3]:
    print("Please enter the correct unique id")

elif input_1 in [1,2,3]:
    if input_1 == 1:
        print("Please let us know what do you want to update for Anuj , use D for diet and E for exercise")
        Var_1= input()
        if Var_1 == "D":
            print("Diet you need to enter")
            diet_you_want_to_enter = input()
            with open("Anuj.diet.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp))
                f.write(" ")
                f.write(diet_you_want_to_enter)
                f.write("\n")
            content = open("Anuj.diet.txt")
            f = content.read()
            print(f)

        if Var_1 == "E":
            print("Exercise you need to enter")
            exercise_you_want_to_enter = input()
            print("Exercise you need to enter")
            with open("Anuj.exercise.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp))
                f.write(" ")
                f.write(exercise_you_want_to_enter)
                f.write("\n")

            content = open("Anuj.exercise.txt")
            f = content.read()
            print(f)

    elif input_1 == 2:
        print("Please let us know what do you want to update for Devanshu , use D for diet and E for exercise")
        Var_1= input()
        if Var_1 == "D":
            print("Diet you need to enter")
            diet_you_want_to_enter = input()
            with open("Devanshu.diet.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp))
                f.write(" ")
                f.write(diet_you_want_to_enter)
                f.write("\n")
            content = open("Devanshu.diet.txt")
            f = content.read()
            print(f)
        if Var_1 == "E":
            print("Exercise you need to enter")
            exercise_you_want_to_enter = input()

            with open("Devanshu.exercise.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp))
                f.write(" ")
                f.write(exercise_you_want_to_enter)
                f.write("\n")
            content = open("Devanshu.exercise.txt")
            f = content.read()
            print(f)




    elif input_1 == 3:
        print("Please let us know what do you want to update for Massive , use D for diet and E for exercise")
        Var_1 = input()
        if Var_1 == "D":
            print("Diet you need to enter")
            diet_you_want_to_enter = input()
            with open("Massive.diet.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp) + " ")
                f.write(diet_you_want_to_enter)
                f.write("\n")
            content = open("Massive.diet.txt")
            f = content.read()
            print(f)

        if Var_1 == "E":
            print("Exercise you need to enter")
            exercise_you_want_to_enter = input()
            with open("Massive.exercise.txt", "a") as f:
                temp = get_date_time()
                f.write(str(temp))
                f.write(" ")
                f.write(exercise_you_want_to_enter)
                f.write("\n")
            content = open("Massive.exercise.txt")
            f = content.read()
            print(f)