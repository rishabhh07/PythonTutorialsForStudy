# Os Module
# My Practice

import os
print(os.listdir("c://"))

# Described by Harry
"""OS modules have a lot of built-in functions. You can see the list of built-in functions we can run through it by 
running the following code, also known as object introspection( For more details, visit tutorial #70):"""

# Built-in Functions               Working
# print(dir(os))                   It gives us a list of all the functions the OS module is composed of.
#                                  Here cwd is a short form for the current working directory.
#                                  The function returns us the path of the directory we are currently

# os.getcwd( ):                    in. It is important to know about our directory because when we are trying to
#                                  import a file in python, the compiler searches for it in our current directory.

# os.chdir( ):                     It is used in case we want to change our directory. The new path is sent inside
#                                  the parenthesis. If we want to access some files or folders from some other
#                                  directory, we can use it.

# os.listdir( ):                   If we want to output the names of all the directories at a certain location,
#                                  we can use this function.

# os.mkdir( ):                     To create a new directory or folder. The name is sent as a parameter inside the
#                                  parenthesis.

# os.makedirs( ):                  To make more than on directory simultaneously.

# os.rename( ):                    To rename an already existing directory, we use this. We send the current name and
#                                  new name of our directory as parameters.

# os.rmdir( ):                     It deletes an empty directory.

# os.removedirs( ):                We can remove all directories within a directory by using removedirs().

# os.environ.get( ):               It will return us the environment variable. The environment variable must be set,
#                                  or the function will return null.

# os.path.join( ):                 It joins one or more path components. We can join the paths by simply using a +
#                                  sign, but the benefit of using this function is that we do not have to worry about
#                                  extra slashes between the components. So less accuracy still provides us with
#                                  the same result.

# os.path.exists( ):               It returns us a Boolean value, i.e., either true or false. It is used to check
#                                  whether a path exists or not. If it does, then the output will be true,
#                                  otherwise false.

# os.path.isfile( ):               It returns true if the path is an existing regular file.

# os.path.isdir( ):                It returns true if the path is an existing directory.


# Summing Up:-
"""In this tutorial, we learned about the OS module with Python 3. The main purpose of the OS module is to interact
with the operating system. The primary use of the OS module is to create folders, remove folders, move folders,
and sometimes change the working directory. OS module has a lot of built-in functions, some of which we've already 
discussed in this tutorial. You can explore more OS module build-in functions by reading its python 
documentation."""

# Code as described/written in the video:

import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))