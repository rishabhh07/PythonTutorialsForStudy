# Join Function

# My Practice
R=["Rishabh", "Shrivastava", "Aayush", "Goel", "Rohan", "Pandya", "Rohit", "Kumar"]

# for item in (R):
#     print(item, "and", end=" ")

# Now same process with join function

a= " and ".join(R)
print(a)



# Described by Harry
string.join(iterable)



#join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# Output:
1, 2, 3, 4



"""The join function has certain limitations.
In the case of the dictionary,
the join function will only return the key part,
separated by the string in between, leaving the value side behind."""
myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))

# Output:
name_separator_country



"""The join function will also not work
when the list or tuple have different type of variables like integer , String, etc."""
inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
sep = '_'
out = sep.join(inputlist)
print(out)
# Output:
Traceback (most recent call last): File "./prog.py", line 3, in TypeError: sequence item 1: expected str instance, int found




# Code file as described in the video
lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = ", ".join(lis)
print(a, "other wwe superstars")
