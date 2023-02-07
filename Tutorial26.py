# args & kwargs
# My Practice
def function_name_print(x,y,z,a):
    print(x,y,z,a)

function_name_print("Rishabh","Rohan", "Aayush","Nishant")

def rishabh(*args):
    print(args[3])

sunny=["Itachi", "Naruto", "Sasuke", "Kakashi",]
rishabh(*sunny)



def rishabh(Raja, *args):
    print(Raja)
    for r in args:
        print(r)

Raja= "Aastey Boliyega"  #This is normal argument, You cant pass the normal argument after "args". i.e (Raja, *agrs)
sunny=["Itachi", "Naruto", "Sasuke", "Kakashi", "Shikimaru"]
rishabh(Raja,*sunny)


# kwargs
def rishabh(Raja, *args, **kwargs):
    print("This is args")
    print(Raja)
    for r in args:
        print(r)
    print("\nThis is kwargs")
    for key,value in kwargs.items():
        print(f"{key} have {value}")

Raja= "Aastey Boliyega"  #This is normal argument, You cant pass the normal argument after "args". i.e (Raja, *agrs)
sunny=["Itachi", "Naruto", "Sasuke", "Kakashi", "Shikimaru"]
rs={"Rishabh":"Bike", "Aayush":"Car", "Rohan":"Scooty", "Adnan":"Paidal"}
rishabh(Raja,*sunny, **rs)




# Code file as described in the video
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)

