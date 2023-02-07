# Jason Module
# My Practice

import json

# json.loads
# x = '{"Sunny":"Bikes", "Rishabh":"Cars"}'
#
# r1= json.loads(x)
# print(r1)
# print(r1["Sunny"])

# json.load
# z = open('data.json',)
#
# data = json.load(z)
#
# for i in data['Emp_Details']:
#     print(i)
#
# z.close()

# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['quiz', 'sport', 'q1']:
    print(i)

# Closing file
f.close()


# Described by Harry
"""If we convert a JSON string to Python, the resultant will be a dictionary. The conversion is also known as parsing, 
and that is the keyword we use professionally for the conversion. We can convert from JSON to Python or Python to 
JSON by using json.loads() or json.dumps() methods. Methods:"""
# load(): This method is used to load data from a JSON file into a python dictionary.
# Loads( ): This method is used to load data from a JSON variable into a python dictionary.
# dump(): This method is used to load data from the python dictionary to the JSON file.
# dumps(): This method is used to load data from the python dictionary to the JSON variable.

# Following is the program showing the use of JSON package in Python
import json
a ={"name":"harry","salary":9000,"language":"Python"}
# conversion to JSON done by dumps() function
b = json.dumps(a)
print(b) # printing the output

# Output:-
# {"name": "harry", "salary": 9000, "language": "Python"}

# What parsing actually does?
"""Parsing converts the code from one form to another, making it compatible with running on the other platform by 
changing all the little syntax differences and making it perfect for running on the other platform. The following 
table shows how Python objects are converted to JSON objects."""
# JSON	   PYTHON
# true     	true
# false   	false
# string    string
# number	number
# array    	list, tuple
# object 	dict
# null      none

# Summing Up:
"""This tutorial has taught us how to create, manipulate, and parse JSON in Python using the JSON module. JSON is 
most commonly used for client-server communication because it is human-readable and easy to read/write. JSON is 
mainly based on key-value pairs, similar to a dictionary in Python. To use the JSON module in Python, we have to 
import it. While using json.dumps(), we can send separators in parameters to make the code more readable and well 
defined. The separators could be full stops, commas, blank spaces, etc."""

# Code as described/written in the video

import json

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
