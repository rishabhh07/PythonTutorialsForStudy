# this code is written by me
print("Driving license age requirement")
print("Enter your age : ")
var1 = int(input())
if var1 > 60:
    print("invalid Age")
elif var1 > 18 :
    print("You're Qualified")
elif var1 == 18 :
    print("You need to come to the driving test then we'll decide what else wo can do")
else:
    print("You're Not Qualified")
