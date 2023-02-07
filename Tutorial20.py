# Using With Block To Open Python Files
# My Practice
with open("Rishabh.txt") as f:
    print(f.read())
    print(f.readline())

f= open("Rishabh.txt")
print(f.readlines(25))
f.close()



With open(“file_name.txt”) as f:



# Code file as described in the video
With open(“file1txt”) as f, open(“file2.txt”) as g

with open("harry.txt") as f:
    a = f.readlines()
    print(a)

# f = open("harry.txt", "rt")
# Question of the day - Yes or No and why?
# f.close()

