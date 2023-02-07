# Using Else With For Loops
# My Practice
Anime = ["Naruto", "One Peace", "Demon Slayer", "My Hero Acadimiya", "Death Note"]
# for item in Anime:
#     print(item)
#     break
#
# else:
#     print("Item Not Found!")

for item in Anime:
    if item in Anime == "Hunter X Hunter": # Hunter x Hunter is not present in the list
        break

else:
    print("Item Not Found!")

"""If we put the break in between then ony first item of list will print then the else will not traverse. Suppose
we want to search any item in present the list and we traverse if statement and then break it and if the item was 
present in the list then else will not traverse and if the item was present in the list then the else will traverse.
"""

# Described by Harry
# How can we implement for-else in Python?
# We have to write an else statement using the Else keyword, followed by a colon after the for loop block of code.
# for x in n:
#    #statements
#  else:
#    #statements

"""Except for these conditions, the program will ignore the else part of the program. For example, if we are just 
partially executing the loop using a break statement, then the else part will not execute. So, a break 
statement is a must if we do not want our compiler to execute the else part of the code."""
# For Example
for i in ['C','O','D','E']:
 print(i)
else:
print("Statement successfully executed")

# Output
# C
# O
# D
# E
# Statement successfully executed


# Code as described/written in the video

khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "rotiroll":
        break

else:
    print("Your item was not found")