

# 1. Create an empty class called "Student"

# class Student:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

<<<<<<< HEAD
#     def greeting(self):
#         print(f"Good morning, {self.first}")
    
#     def full_name(self):
#         print(f"{self.first} {self.last}")

# stud_1 = Student('Andrea', 'Myers')
# stud_2 = Student('Ally', 'Smith')
# stud_3 = Student('Kanny', 'Jones')
# stud_4 = Student('Kim', 'Roberts')
# stud_5 = Student('Veronica', 'Lino')


# Student.greeting(stud_1)
# Student.greeting(stud_2)
# Student.greeting(stud_3)
# Student.greeting(stud_4)
# Student.greeting(stud_5)



# 2. 5 students objects (instances of the class "Student") of "Student" types
=======
#2. Create 5 students objects (instances of the class "Student") of "Student" types
>>>>>>> 915f1d5b41201c1da6377b24f8dee08c0bb9cfa7


#3a. Create a "greeting" method inside of the class "Student" class that 
# takes as a parameter "name". The return of the  method should be
# "Good morning {name}" 


#4. Call the greet  method on each of the students in # 5 passing in a different
# name argument each time.

#5a. Create a constructor for the Student class. 
#5b. Create a print statement inside of the constructor
#5c. Run your lab.py again and you should see a print statement for each student object 
# That you created 


#6a. Pass in "name" as a parameter to your Student constructor. 
#6b. Create an instance variable for name
#6c. Refactor your greeting method by removing the name parameter and 
# adding a "self" in front of the printed "name" variable in the return statement 
#6d. Refactor your Student objects by passing in the name as an argument when the
# object gets instantiated 

#7. Class Methods
#7a. Create a "Class" method inside of the "Student" called "campus" that returns the 
# Statement "Digital Crafts - Houston"
# Campus is a "Class" method so it should not have "self" as an argument. 
#7b. call the campus method by invoking Student.campus()
#7c. Call the campus method on each of the student objects 
#7d. Return the name of the student in the campus method (instance variable) (you should
# get an error)

#8. Class Variables 
#8a. Create a class variable inside of the Student class called "cohort" whose value is
# "June 2020 Cohort"
#8b. Print to the console each class variable for each of the student objects, i.e. 
# Michah.cohort 
#8c. Refactor your class method to print out the class variable when it is called 
#8d. Call the class method on the class (i.e. Student.campus())
#8e. Call the class method on each object (i.e. Dan.campus())

#9. Accessor Modifiers 
# Refactor your constructor to take a parameter for studentID
#9a. Create a new instance variable for studentID with the value _studentID
# Refactor the student objects to pass a studentID argument
#9b. Print the studentID value to the console
# Change the value of studentID to __studentID 
# Print the value to the console (you should get an error)


#. Inheritance 

# Create a new class called Car with the following method :
# CarDetails which prints "Here are details of this car"

# Create a new class called Hybrid that inherits from the Car class
#  with the following method: CarType which prints "I am a hybrid car" 


# Create a new class called Electric that inherits from the Car class
#  with the following  method: CarType which prints "I am a hybrid car" 

# Create a Hybrid instance and an Electric instance
# Call the method CarType on the Hybrid Instance and Electric Instance 
# Call the method Car Details on each instance
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def carDetails(self):
        print(f"Here are details of this car:\n make: {self.make}\n model: {self.model}\n color: {self.color}")

# the child Hyrid is inheriting from the parent Car
class Hybrid(Car): 
    
    def carType(self):
        print("I am a hybrid car")

class Electric(Car): 
    
    def carType(self):
        print("I am an Electric car")

prius = Hybrid('Toyota', 'prius', 'lime green')
tesla = Electric('Tesla', 'ModelS', 'sky blue')

print(prius.make)
prius.carType()
prius.carDetails()

print(tesla.make)
tesla.carType()
tesla.carDetails()




# Add the following instance variables to the Car class :
# - make 
# - model 
# - color








# Implicit Inheritance 

#. Override Explicitly

# Alter Before or After

# Super()

# COMPOSITION


<<<<<<< HEAD




# class Counter:
#     def __init__(self):
#         self.count = 0

#     def incrementCount(self):
#         self.count += 1
#         return self.count

# count1 = Counter()

# print("count 1", count1.incrementCount())
# print("count 1", count1.incrementCount())
# print("count 1", count1.incrementCount())
# print("count 1", count1.incrementCount())
# print("count 1", count1.incrementCount())

# count2 = Counter()

# print("count 2", count2.incrementCount())
# print("count 2", count2.incrementCount())
# print("count 2", count2.incrementCount())

# print("count 1", count1.incrementCount())

## Using objects through a class allows you to keep track of the data in memory. 
# Functions don't keep track of anything, once its over the data is gone


#### Creating a new class 'of person type'

# class Person:
#     def __init__(self, first, last, birthdate, address, phone, email):
#         self.first = first
#         self.last = last  
#         self.birthdate = birthdate 
#         self.address = address
#         self.phone = phone
#         self: email = email 
    
#     def age(self):
#         pass


# person1 = Person('Andrea', 'Myers', '1/1/2005', '123 sesame st', '333-333-3333', 'andream.gmail.com')

# person1.age()

######## Another practice class

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
    
#     def greet(self, other_person):
#         print(f"Hey, {other_person.name}. Welcome. My name is {self.name}.")

#     def contact_info(self):
#         print(f"What to contact {self.name}?\nEmail: {self.email} Phone: {self.phone}")


# sonny = Person('Sonny', 'sonny@hotmail.com','123-456-6789')
# jordan = Person('Jordan', 'jordan@aol.com', '987-654-3245')


# sonny.greet(jordan)
# jordan.greet(sonny)

# # sonny.contact_info()
# # jordan.contact_info()
# ###alternate way to call to the class methods 
# Person.contact_info(sonny)
# Person.contact_info(jordan)
=======
>>>>>>> 915f1d5b41201c1da6377b24f8dee08c0bb9cfa7
