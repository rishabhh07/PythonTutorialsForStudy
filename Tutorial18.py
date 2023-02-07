# # My practice
#
# # To write some on file
# # f= open("Rishabh.txt", "w")
# # content= f.write("Itachi Uchiha")
# # f.close()
#
# # To read some thing in file
# f= open("Rishabh.txt", "r")
# print(f.readline())
# print(f.readlines())
# content= f.read()
# print(content)
# f.close()
#
# # To append in file
# # f= open("Rishabh.txt", "a")
# # content= f.write("Mangekyo Sharingan\n")
# # f.close()
#
# # To see the charecters in file
# f= open("Rishabh.txt", "a")
# content= f.write("Mangekyo Sharingan\n")
# print(content)
# f.close()



# Code file as described in the video
# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("harry2.txt", "r+")
print(f.read())
f.write("thank you")

