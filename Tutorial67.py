# Python 'is' vs '==': What's The Difference?
# My Practice
a = [6,4, "34"]
b = [6,4, "34"]
print(b is a)

# Described by Harry

# Equality operator (==) in Python:
"""'==' is used to represent value equality. Value equality means two variables or objects or even data structures such as 
a list composed of the same value. Suppose we have two variables, a and b. We assign the value 2 to both of them. 
Now, as we know that they do not have any direct link with each other. The only similarity is that they have been 
given the same value. So, if we place an '==' sign between them, the output will be True. However, when we change 
the value of one of the variables, it will return false."""
# For Example:-
x = [1, 2, 3, 4]
y= [1, 2, 3, 4]
x == y
#True
# In this example, 'x == y' returns true because what x is referencing contains the same things that y is referencing.


# Identity operator (is) in Python:
"""'is' is generally used to denote reference equality. The data structure or variables in the case has to be the same. 
In the case of the object, the objects must be referring to the same kind of data. In case we use a copy of our 
variable or data structure or even make a similar one with the same values, it will still return False as their 
reference is not the same. For example, if we assign a list to two different objects, the 'is' keyword will return 
true as they refer to the same list. If we change an entry in the list, it will also be changed for the other one, 
so no change in output."""
# For Example:-
c = [1, 2, 3]
d = [1, 2, 3]
c == d #True
c is d #False

# When we assign a list to a variable, Python allocates memory for that list, but the actual list is not stored in our
# variable. Instead, Python creates a list object and stores a reference to that object in the variable. However,
# in the above example, c = [1, 2, 3, 4] and d = [1, 2, 3, 4]
#
# This creates a list object and stores a reference to it in c; then, it creates a second list object and stores a
# reference to it in d.
#
# ‘c == d’ is still true. However, 'c is d' is now false. This is because both c and d refer to different objects.
#
# So, to recap the difference between "is" and "==" into short definitions:
#
# An identity operator(is) expression evaluates to True if two variables point to the same object.
# An equality operator ( == )expression evaluates to True if the objects referred to by the variables have the same
# contents.
# The identity operator 'is' tracks the object back to its identity while the equality operator '==' only compares
# the values.

# Code as described/written in the video:


# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a =[6, 4 , "34"]
b = [6, 4 , "34"]
print(b is a)
