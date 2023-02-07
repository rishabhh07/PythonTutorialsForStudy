# Scope, Global Variables and Global Keyword
# My Practice
x=7
def Rishabh():
    x=5
    def Sunny():
        global x
        x = 10
    print("Function1", x)
    Sunny()
    print("Function2", x)

Rishabh()
print(x)



# x=24
# def rohan():
#     r=24
#     def aayush():
#         global x
#         x=97
#     print("They are good friends", r)
#     aayush()
#     print("nasta bolyega",x)
# rohan()
# print(x)


def sum():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    sum = a + b
    print(sum)


print(a)  # this gives an error





a=1  #global variable

def print_Number():

            a=a+1;
            print(a)

 print_number()





# Code file as described in the video
# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)