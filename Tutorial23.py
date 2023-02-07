# Lambda Functions or Anonymous Functions
# My practice
# def multply(a,b):
#     return (a*b)
# print (multply(5,6))


multply= lambda a,b:a*b
print(multply(5,4))

def devide(x,y):
    return (x/y)
print(devide(2,4))


devide= lambda x,y:x/y
print(devide(2,4))




def function_name ():



result = lambda n1, n2, n3: n1 + n2 + n3;
print("Sum of three values : ", result(10, 20, 25))



list.sort(key=myFunc ,reverse=True|False)




# Code file as described in the video

# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)

