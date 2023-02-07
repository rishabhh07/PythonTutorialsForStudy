# k=int(input())
# # if k ==
# for i in range(1,5):
#     print(i)
# Solution type1
# print("Enter you Number")
# var1= int(input())
# print("Type 0 or 1 ")
# var2= int(input())
# var3= bool(var2)
# if var3 == True:
#     for i in range (1,var1+1):
#         for j in  range (1, i+1):
#             print("*",end=" ")
#         print()
# elif var3 == False:
#     for i in range (var1,0,-1):
#         for j in range (1, i+1):
#             print("*", end=" ")
#         print()


# Solutipon type2
# print("Enter your number")
# var1 = int(input())
# print("type 0 or 1")
# var2 = int(input())
# var3 = bool(var2)
# if var3 ==True:
#     for i in range (1, var1+1):
#         print("* "*i)
# if var3 == False:
#     for i in range (var1,0,-1):
#         print("* "*i)



# This program with function
a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False")))


def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "* ")
            c = c + 1
    else:
        while a > 0:
            print(a * "* ")
            a = a - 1


star(a, b)