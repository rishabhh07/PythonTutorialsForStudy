# Using External & Builtin Moudule
# Random Moudule
# My Practice
# import random
# var1 = random.randint(1,100)
# print(var1)
#
# var2= random.random()
# print(var2)
#
# lst= ["Cartoon Network", "Pogo", "Hangama", "Disney"]
# Choice= random.choice(lst)
# print(Choice)





# Code file as described in the video
# import random
#
# random_number = random.randint(0, 1)
# # print(random_number)
# rand = random.random() * 100
# # print(rand)
# lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
# choice = random.choice(lst)
# print(choice)
#





# Random Number Guessing Game
import random
import sys

random_number=random.randint(0,10)
m=int(input("Choose the no between 0-10 \nEnter the no here "))
if m>10:
    print("Please enter the no between 0-10 ")
    sys.exit()
else:
    pass
if random_number==m:
    print("Its correct :)")
else:
    print("You lost :( correct ans is ", random_number)
