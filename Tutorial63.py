# Pickle Module
# My Practice

import pickle

# Pickling
# Car_Brands = ["Mercedes Benz", "BMW", "Audi", "Aston Martin", "Maserati" "Toyota",
#               "Subaru", "Infinity", "Lamborghini", "Ferrari", "McLaren"]
#
# File = "Mycars.pkl"
# FileObj =open(File, "wb")
# pickle.dump(Car_Brands, FileObj)
# FileObj.close()

# Open Pickle file
# file = open("Mycars.pkl", "rb")
# my_cars = pickle.load(file)
# print(my_cars)

# Pickle.loads
Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
         'age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
           'age': 50, 'pay': 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
b = pickle.dumps(db)  # type(b) gives <class 'bytes'>

# For loading
myEntry = pickle.loads(b)
print(myEntry)


# Code as described/written in the video

import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?