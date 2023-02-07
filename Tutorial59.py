# Coroutines In Python
# My Practice
# 1 Exercise

import time
def Khoj():
    time.sleep(5)
    Everything = "Hare Krishna Hare Krishna, Krishna Krishna Hare Hare, Hare Ram Hare Ram, Ram Ram Hare Hare"

    while True:
        text =(yield )
        if text in Everything:
            print("Yes, Your text is in the Everything")
        else:
            print("No, Your text is not in Everything")

K = Khoj()
print("Reading Whole Universe...")
next(K)
K.send("Rishabh")
input("Press Any key Continue")
K.send("Krishna")
input("Press Any key Continue")
K.send("Ram")
input("Press Any key Continue")
K.send("Ram")
K.close() # After this the program will not run


# Described by Harry
"""Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning 
or deep learning algorithms, or in cases where the program has to read a file containing a large number of data. 
In such situations, we do not want the program to read the file or data again and again, so we use coroutines to 
make the program more efficient and faster. Coroutines run endlessly in a program because they use a while loop 
with a true or 1 condition, so it may run until infinite time. Even after yielding the value to the caller, it 
still awaits further instruction or calls. We have to stop the execution of the coroutine by calling the coroutine.
close() function. It is crucial to close a coroutine because its continuous running can take up memory space, as 
we have discussed in Tutorial #75, related to function caching. We can define a coroutine using the following
statements."""
def myfunc():
    while True:
        value = (yield)


# Coroutine Execution:-
"""Execution is the same as of a generator. When you call a coroutine, nothing happens. They only run in response 
to the next() and send() methods. Coroutine requires the use of the next statement first so it may start its 
execution. Without a next(), it will not start executing. We can search a coroutine by sending it the keywords 
as input using object name along with send(). The keywords to be searched are send inside the parenthesis."""

"""When we run the next() function the first time, the coroutine executes and waits for new input. After the 
input is sent to it using the send() function, it executes it and again waits for next input, and the process 
goes on like this because we have set the while loop as true, so it will never exit its execution. In order to 
make the execution stop, we have to close the coroutine using coroutine.close() function."""
# send() — used to send data to coroutine
# close() — to close the coroutine
# Example:
def myfunc():
    print("Code With Harry")
    while True:
        value = (yield)
        print(value)

coroutine =myfunc()
next(coroutine)
coroutine.send("Python")
coroutine.send(" Tutorial ")
coroutine.close()

# Output:-
# Code With Harry
#  Python
#  Tutorial

"""After closing the coroutine, if we send values, it will raise the StopIteration exception. Coroutines are 
used for data processing mechanisms. Coroutines are similar to generators, except they wait for information to 
be sent to it using send() function."""


# Code as described/written in the video

def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")