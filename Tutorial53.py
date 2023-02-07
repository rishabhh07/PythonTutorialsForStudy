# Oop17/Object oriented programming
# Object Introspection
# My Practice

# Object Introspection in Python:
"""Introspection can be said as the ability to recognize the object along with all its details,
such as id or location at runtime. One of the most basic introspects we came across many times earlier is type()."""
type(object)
"""We used it to see the type of our object, that whether it is int, float, or string. 
We have to pass the object in the parenthesis, and the compiler will return the type. 
Introspection gives us useful information about the program’s objects. 
Python provides tremendous introspection support. 
Introspection is the ability to determine the type of an object at runtime. 
Hence, by using introspection, we can inspect the Python objects dynamically."""


""""Id provides us with the id allocated to the particular object. The id of each object is unique, 
meaning it is different, and no two objects can have the same id."""
id(object)


"""Now the most important introspection function is dir(). It returns us a list of attributes and methods associated 
with an object. By using dir(), we can check the attributes that our object is composed of. 
It is mostly executed before and after updating our object by inserting more attributes or methods."""
# o = MyClass()
# print(dir(o))



# Types of introspects:-
# Some of the other common Introspects:

# Functions	         Working
# hasattr()	It checks if an object has an attribute.
# getattr()	It returns the contents of an attribute if there are some.
# repr()	It returns the string representation of an object
# vars()	It checks all the instance variables of an object
# issubclass()	This function checks that if a specific class is a derived class of another class.
# isinstance()	It checks if an object is an instance of a specific class.
# __doc__	  This attribute gives some documentation about an object
# __name__	This attribute holds the name of the object
# callable()	This function checks if an object is a function
# help()	It checks what other functions do



# Code as described/written in the video:

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)
o = "this is a string"
# print(dir(skillf))
# print(id("that that"))

import inspect
print(inspect.getmembers(skillf))