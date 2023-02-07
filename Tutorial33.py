# Map function
# My Practice
# L1= [25, 65, 78, 25]
# a= list(map((lambda x:x+x),L1))
# print(a)
#
#
#
# L1= [25, 65, 78, 25]
# L2 = [1,5,6,7]
# a= list(map((lambda x,y:x+y),L1,L2))
# print(a)



# Filter Function

# R1=[2,3,4,1,7]
# R2=[2,5,7,8,9]
# R3= list(filter(lambda x:x in R1,R2))
# print(R3)
#
#
# a=["Rishabh", "Rohan", "Aayush", "Rohit", "Sunny"]
# b=["Rishabh", "Paand", "Sunny", "Gwala", "Dabbu"]
# c= list(filter(lambda x:x in a,b))
# print(c)


# Reduce
# You dont need to typecast the whole function into list in reduce function
from functools import reduce
a= reduce(lambda x,y:x+y,[5,6,7,5,4,8,9])
print(a)


from functools import reduce
a= reduce(lambda x,y:x*y,[5,6,7,5,4,8,9])
print(a)


from functools import reduce
a= reduce(lambda x,y:x-y,[5,6,7,5,4,8,9])
print(a)


from functools import reduce
t=[5,6,7,5,4,8,9]
a= reduce(lambda x,y:x*y,t)
print(a)



# Described by Harry
map(function, iterable)

items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x **3), items))
print(a)
#Output: [1, 8, 27, 64, 125]



filter(function, iterable)

a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c) # prints out [2, 5, 3]



reduce(function, iterable)

from functools import reduce
a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a)
#Output: 24





# Code file as described in the video
# --------------------------MAP------------------------------
# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# print(square)
# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# --------------------------FILTER------------------------------
# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)
# --------------------------REDUCE------------------------------
from functools import reduce

list1 = [1, 2, 3, 4, 2]
num = reduce(lambda x, y: x * y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)


