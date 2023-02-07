# Oop16/Object oriented programming
# Setters & Property Decorators
# My Practice
class Team:
    def __init__(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def captains(self):
        return f"The Captain and Vice Captain of team India is {self.captain} & {self.vice_captain}"

    """property decorator converts the function into a attribute now this function will work as a attribute 
    we don't need to give parenthesis "()" to the functions we simply write the name of the function for printing.
    We Encapsulate the function by using property decorator."""
    @property
    def base(self):
        return f"{self.captain} & {self.vice_captain} are the pillars of the team"

    """Setters are a great way of performing encapsulation. So by using setter, our interaction gets limited
     to the decorator, making the use of encapsulation concept, which is the basis of Oop. 
     We can set new values for a newer object or update values for an older one."""
    @base.setter
    def base(self, string):
        print("Changing Now...")
        name = string.split("are")[0]
        self.captain = name.split("&")[0]
        self.vice_captain = name.split("&")[1]

    """Deleter is used to delete the values passed as a parameter before. 
    We can use a setter if we want to update or change the value, but we can not use it to delete the value. 
    This is where deleter comes in; it removes the previous value and sets the variable equal to none. As in OOP, 
    we do not completely erase the existence of some variable but sets it equal to none."""
    @base.deleter
    def base(self):
        self.captain = None
        self.vice_captain = None

Captains_Name = Team("Virat Kohli", "Rohit Sharma")

print(Captains_Name.captains())
print(Captains_Name.base)
# Captains_Name.vice_captain = "KL Rahul"
print(Captains_Name.captains())
Captains_Name.vice_captain = "KL Rahul"
print(Captains_Name.base)
Captains_Name.base = "MS Dhoni & Virat Kohli are the pillars of the team"
print(Captains_Name.base)
del Captains_Name.base
print(Captains_Name.base)

# Described by Harry
# Use @property along with the getter method to access the value of the attribute.
# @property
# def getter method


# function_name.setter is a setter method with which we can set the value of the attribute
# @function_name.setter
# def function


# @function_name.deleter is a deleter method which can delete the assigned value by the setter method
# Deleter method
# @function_name.deleter


# Code as described/written in the video
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


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)