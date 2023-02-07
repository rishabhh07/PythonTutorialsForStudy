# If __name__==__main__ usage & necessity
# My Practice
# See Temp3
import temp3
print(temp3.add(7, 5))




# Described by Harry
#tutmain1.py
print("__name__ in tutmain1.py is set to"+__name__)



__name__ in tutmain1.py is set to __main__



#tutmain2.py
import tutmain1

print("__name in tutmain2.py is set to"+__name__)



__name__ in tutmain2.py is set to tutmain1



if__name__=="__main__":
    #Logic Statement



# Code file as described in the video
def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("and the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)

