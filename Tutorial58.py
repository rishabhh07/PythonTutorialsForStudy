# Else & Finally In Try
# My Practice
# R = open(Rishabh.txt)
f1 = open("Rishabh.txt")

try:
    f= open("ram.txt") # This file is not on the list

except Exception as e:
    print(e)

else:
    print("This will only run when except is not running")

finally:
    print("Jai Shree Krishna")
    f1.close()
    # f.close()

print("Jai Shree Ram")


# Described by Harry
# else keyword:-
""""We use an else keyword to print something in cases where no exception occurs. Suppose that an exception 
occurred, and the except block is printing the error; likewise, if the exception does not occur, we can print 
a statement that no error occurred, using an else keyword. Syntax of using else with try and except block is:"""

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
    #No Exception. Run this code
# Note: An else will only run in the case where no exception occurs.

# For Example:-
    def divide(a, b):
        try:
            print(f'{a}/{b} is {a / b}')
        except ZeroDivisionError as e:
            print(e)
        else:
            print("No Exception")


    divide(1, 2)
# Output :-
#  1/2 is 0.5
# No Exception

# finally:-
"""Now the last keyword for this tutorial, i.e., finally, will run in either case. It is also known as code 
cleaner because it will perform its action, either an exception occurs or not. We write such commands in the 
finally part of the code that we want to execute, even an exception occurs or not. It is mostly used to clean 
resources or close files."""
try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
   #No Exception. Run this code
finally:
   #Always run this code

"""Now, in cases where all the four keywords are being used simultaneously, which will run and which will not, 
can easily be understood by the table below:"""

# Try           Not Running        Running
# Except        Will Run           Will Not Run
# Else          Will Not Run       Will Run
# Finally       Will Run           Will Run


# Code as described/written in the video
f1 = open("harry.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")