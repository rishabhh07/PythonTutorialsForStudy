#Practice
#This is built in function
a=5
b=7
c= sum((a,b)) #tuple (This should be itrable)
d= sum([a,b]) #list (This should be itrable)
#print(c,d)

#User define functions
def function1():
    print("Aastey Boliyega!")

print(function1())

function1()
function1()
function1()
function1()
function1()

# Functions also can take input
def function1(a,b):
    print("Aastey Boliyega!", a+b)

function1(5,7)

# If we want to the value in variable
def function2(a,b):
    average=(a+b)/2
    print(average)
function2(5,7)


#if we want to store the function in variable
def function2(a,b):
    average=(a+b)/2
    return average
v=function2(5,7)
print(v)


print(v)


#Docstring
"""We give Docstring to define the specific so the user can understand how this function works"""

def function2(a,b):
    """this is the function which will calculate the average of two numbers"""
    average=(a+b)/2
    return average
v=function2(5,7)
print(v)



#Harry code
#Code file as described in the video
# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function2.__doc__)
