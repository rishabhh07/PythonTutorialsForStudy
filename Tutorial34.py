# Decorators in Python
# My Practice
# def Rish1(func):
#     def Rish2():
#         print("Rishabh is a good boy")
#         func()
#         print("Rishabh is awesome")
#     return Rish2
#
# @Rish1
# def Rish3():
#     print("Sunny")
#
# Rish3()



def sun1(rs):
    def sun2():
        print("Jai Shree Ram")
        rs()
        print("Jai Shree Krishna")
    return sun2

@sun1
def sun3():
    print("Ram Ram")

sun3()




# Decribed by Harry
def inner1(func):
    def inner2():
        print("Before function execution");
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")

function_to_be_used()


# Output:
# Before function execution
# This is inside the function
# After function execution





# Code file as described in the video
# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
#
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec


@dec1
def who_is_harry():
    print("Harry is a good boy")


# who_is_harry = dec1(who_is_harry)

who_is_harry()


