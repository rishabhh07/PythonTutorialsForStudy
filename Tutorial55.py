# Python Comprehensions
# My Practice
# 1 Exercise

# Rs=[]
# for i in range(3,150):
#     if i%3==0:
#         Rs.append(i)

# print(Rs)

# List Comprehension
Rs=[i for i in range(3,150) if i%3==0]
print(Rs)


# Dictionary Comprehension
Dict1 = {r:f"Rishabh {r}" for r in range(150)}
Dict2 = {r:f"Rishabh {r}" for r in range(150)}
Dict2 = {value:key for key,value in Dict2.items()} #To reverse the Dictionary
print(Dict1,"\n",Dict2)


# Set Comprehension
Sun={Sun for Sun in ["Rishabh1", "Rishabh1", "Rishabh1", "Rishabh1"]}
print(type(Sun))
print(Sun)


# Generator Comprehensions
S=(i for i in range(3,150) if i%3==0)
print(S.__next__())
print(S.__next__())
print(S.__next__())
print(S.__next__())



t=(1,5,4,2,4,67,8,1,1,5,7)
print(type(t))

# TEMP Exercise
no_of_list = int(input("How many items add in a list: "))
input_string = input("Enter a list element separated by space ")
list = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in list}
    print(s)
    print(type(s))

# Exercise by me



# Described by Harry

# List as ordinarily are written as such:
 listA = []
 for a in range(50):
     if a%5==0:
         listA.append(a)

# While it can be written in a one liner format using comprehension as such:
listA = [a for a in range(50) if i%5==0]


"""The syntax is almost the same as List, except for the brackets i.e. set uses curly brackets. The main difference arrives 
while printing the items as a set will only print the same items once. """
alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
# The output will be: {'a', 'b', 'c', 'd'}


# The syntax for a dictionary using ordinary syntax is:
Normaldict = {
  0 : "item0",
  1 : "item1",
  2 : "item2",
  3 : "item3",
  4 : "item4",
}
# And the more compact one is:
Compdict = {i:f"Item {i}" for i in range(5)}


# We can implement comprehension on generators too.
def gener(n):
    for i in range(n):
        yield i

a = gener(5)
print(a.__next__())


# We can also create a one liner for generators too by following the syntax below.
gener = (i for i in range(n))
a = gener(5)
print(a.__next__())


# Code as described/written in the video

# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# dresses = [dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]]
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

# for item in evens:
#     print(item)