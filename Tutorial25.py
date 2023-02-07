# F string and String formation
# My practice
from datetime import date
a= "Rishabh"
b= "Sunny"
c= 5
var1= f"This is {a},{b},{c}, {date.today()}"
print(var1)


# String formating
z= "Rishabh is a {}"
str= z.format("good boy")
print(str)



# name="Jack”
#
#  n="%s My name is %s” %name
#
# print(n)
#
#  # Output: "My name is Jack."
#
#
#
#
# name=”Jack”
# class=5
# s=”%s is in class %d”%(name,class)
# print(s)
# # Output: Jack is in class 5.
#
#
#
#
# str = "This article is written in {} "
#
# print (str.format("Python"))
# # Output: This article is written in Python.
#
#
#
#
# ## declaring variables
#
#  str1="Python”
#
#  str2="Programming”
#
# print(f"Welcome to our {str1}{str2} tutorial”)
# # Output: Welcome to our Python Programming tutorial.
#
#
# import time
#
#
#
# # Code file as described in the video
# # F strings
# import math
#
# me = "Harry"
# a1 = 3
# # a = "this is %s %s"%(me, a1)
# # a = "This is {1} {0}"
# # b = a.format(me, a1)
# # print(b)
# a = f"this is {me} {a1} {math.cos(65)}"
# # time
# print(a)

