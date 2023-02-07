# Creating a Command Line Utility In Python
# My Practice
import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'mult':
        return args.x * args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Somthing went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help= "Enter The First Number. This is the utility for calculation. Please contact Rishabh")
    parser.add_argument('--y', type=float, default=3.0,
                        help= "Enter The Second Number. This is the utility for calculation. Please contact Rishabh")
    parser.add_argument('--o', type=str, default="add",
                        help= "This is the utility for calculation. Please contact Rishabh")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

# I need to make faultycalculator calculator with the help of command line interface (CLI).


# Described by Harry
# What Is a Command Line Utility?
"""A command-line utility is a way of giving operating system instructions using lines of text. Command-line
programs operate via the command line or PowerShell. It will interact with a command-line script.
Now let us come to why we should use the command-line utility in our program. We can easily call a command line program 
in Python or any other language into a different language program. Each program has calling support in it for 
calling the command lines program. So in cases, where we are writing a program in some other language, but 
we want to perform a task in Python and call it in our program, then the command line can help us do that."""
"""Now we are going to discuss how part of this tutorial. For creating a Command Line Utility In Python, first import two 
modules, i.e., argsparse and sys. argsparse helps us to get command-line arguments in our program, and the sys 
module helps us to import the code we wrote using argparse onto the console. For more details and descriptions 
about these modules, you can read the python documentation for these modules."""
import argparse
import sys

# What is argparse?
"""Python comes with several different libraries that allow us to write a command-line interface for our scripts, but the
standard way for creating a CLI in Python is by using the Python argparse module. The argparse module helps us to
parse the arguments passed with the script and process them more conveniently. One of the advantages of using the
argparse module is that it makes it easy to write user-friendly command-line interfaces.

We can use the Python argparse module to create a command-line interface by following these steps:

1.Import the Python argparse module
2.Create the parser
3.Add optional and positional arguments to the parser
4.Execute .parse_args()
When we execute .parse_args(), we will get the Namespace object that contains a simple property for each input
argument received from the command line. In this tutorial, we are going to use the Argumentparser class
available in the argparse module. We fill ArgumentParser with information about program arguments by
making calls to the add_argument() method."""

# What is the sys module?
"""Python provides the sys module that gives us independence from the host machine Operating System and allows us to 
operate on an underlying interpreter, irrespective of its being a Linux or Windows Platform. With the help of the 
sys module, we can access system-specific parameters and functions. It provides different functions used to 
manipulate different parts of the Python Runtime Environment. To use the sys module, we have to import it so that 
it brings required sys module dependencies into our scope."""

# Code as described/written in the video

import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
