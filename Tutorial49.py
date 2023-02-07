# Oop13/Object oriented programming
# Diamond Shape Problem In Multiple Inheritance
# My Practice
# Access this to watch the image
# https://cwh-full-next-space.fra1.digitaloceanspaces.com/videos/python-tutorials-for-absolute-beginners-66/base64.webp
class R:
    def ram(self):
        print("Jai Shree Ram")

class I(R):
    def ram(self):
        print("Jai Shree Ram 1")

class S(R):
    def ram(self):
        print("Jai Shree Ram 2")

class H(I, S):
    # def ram(self):
    #     print("Jai Shree Ram 3")
    pass


a = R()
b = I()
c = S()
d = H()

print(d.ram()) # It will print the first argument of its class for example it will print the constructor of I.




# Described by Harry
# Explanation:-
"""In the above image, we can see that class C and class B are inheriting from class A, 
or it can be said as class A is a parent to class B and C. And class D is inheriting from both class C and B. 
So, in a way, they are all in relation to one and other somehow. 
Let us write down the relation in code format so it will be easier to understand. """

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D( B, C ):
    pass

# If the C class would be on the left, such as

 class D( C,B ):
       pass

# Then priority would be given to C.

"""Sometimes, when we are working with too many classes, the concept of multiple inheritance could make our code 
more confusing and difficult to understand, such as:"""

# Code as described/written in the video
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()