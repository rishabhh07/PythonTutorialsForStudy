# Generators In Python
# My Practice

def generator(n):
    for i in range(n):
        yield i

g = generator(500)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

# for c in g:
#     print(c)

r = generator(200)
for w in r:
    print(w)

q = "Rishabh" # We can iterate the value one by one by using __next__ method.
e = iter(q) # it makes the value iterable.
print(e.__next__())
print(e.__next__())
print(e.__next__())
# for f in e:
#     print(f)

# q = 80  # integer object in not iterable
# e = iter(q)
# for f in e:
#     print(f)



# Described by Harry
"""Iterables are objects that can be placed inside a loop and can return one variable at a time. 
In simple terms, we can say that iterables are objects capable of iteration. 
Examples of iterable include list, string, tuple, etc."""
for c in a:
      print (a)
#Here a is an iterable.



# What are the Generators in Python?
"""Generators concept is also very similar as it is used to make an iterator. 
The only difference comes in the return statement. The generator does not use a return statement. 
Instead, it uses a yield keyword. Yield functionality is very similar to return as it returns a value to the caller,
but the difference is that it also saves the state of the iterator. 
Meaning that when we use the function again, the yield will resume the value from the place it left off. """

"""Generators in Python are created just like the normal functions using the ‘def’ keyword. Generator functions 
do not run by their name, and they are run when the __next__() function is called. A generator is very helpful 
in projects relating to memory issues because, like a simple iterator, it does not return all the values at a 
time; instead, it produces, series of values over time. So a generator is generally used when we want to iterate 
over a series of values but do not want to store them completely in memory. """

# For Example:
def getNum (x):
    for i in range(x):
        yield i

seq = getNum (2)
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# Output:
0
1
Traceback (most recent call last):
File "<stdin>", line 7, in <module>
 print(seq.__next__())
StopIteration



# Code as described/written in the video:
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)