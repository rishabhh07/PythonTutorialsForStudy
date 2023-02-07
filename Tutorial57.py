# Function Caching In Python
# My Practice
import time
from functools import lru_cache    # lru_cache is a decorator

@lru_cache(maxsize=5)
def Rishabh_Work(n):
    # Rishabh_Work task taking n secs
    time.sleep(n)
    return n

if __name__=="__main__":
    print("Now program is running")
    Rishabh_Work(5)
    Rishabh_Work(2)
    Rishabh_Work(8)
    Rishabh_Work(9)
    print("Done Running. Calling Again")
    Rishabh_Work(2)
    print("Finally Completed")

# Exercise Done by user
import time
from functools import lru_cache
p = int(input("Set the maxsize for the @lru_cache: "))
@lru_cache(maxsize=p)
def time_delay(n1):
    for i in range(5):
        print(i)
        time.sleep(n1)


time_delay(3)
print("Done")
time_delay(3)
print("Memory is cached...")

# Exercise Done by me

# Described by Harry
# How to use function caching in Python?
""""Function caching is a way to improve code's performance by storing the function's return values. Before the 3.2 
updates of Python, we had to create a cache ourselves by storing the value in a variable or by other such means. 
But in Python 3.2, there is a new update in the functools module of Python. To use this module, we have to 
import it first."""
import functools

"""We have to pass maxsize as a parameter with the decorator. maxsize is defined to tell the program how many values we 
want to store in the cache. It automatically stores the values for the latest number of calls."""
# For example
@functools.lru_cache(maxsize=4)
def myfunc(x):
    time.sleep(2)
    return x

myfunc(1)
# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
myfunc(2)
myfunc(3)
myfunc(4)
myfunc(5)


# Code as described/written in the video

import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")