# school = "Digital Crafts"
# print(school)

#quick copy of lines of code = shift + option + down arrow
# command + forward slash to comment out blocks of code
 
# string formating 

# student1 = "Andrea"
# student2 = "Zach"
# student3 = "Michael"
# student4 = "Rick"

# "".format() the dot accesses the methods that are avaiable for the string object

# "{} {} {} {}".format(student1, student2, student3, student4)
# # we can assign this to a variable because it is just a formated string
# formatting = "{} is the best. {} is a common name. {} is a cool guy. {} is very nice.".format(student1, student2, student3, student4)
# print(formatting)



# how to change the order of the strings = put numbers in the brackets

# formatting = "{3} is the best. {0} is a common name. {2} is a cool guy. {1} is very nice.".format(student1, student2, student3, student4)
# print(formatting)

#you can put one string 4 times 
# formatting = "{0} is the best. {0} is a common name. {0} is a cool guy. {0} is very nice.".format(student1, student2, student3, student4)
# print(formatting)

# creating a variable inside the method 
# formatting = "{Andrea} {Zach}".format(Andrea=student1, Zach=student2)
# print(formatting)





# # f strings = f stands for format (this way is quicker)
# day = "Wednesday"
# tomorrow = "Thursday"

# # f"Today is {day}" this is a string

# current_day = f"Today is {day}"
# next_day = f"Tomorrow is {tomorrow}"

# print(current_day)
# print(next_day)





# type function = tells you the type of the data object

# print(type("Hello World")) # tells us that the class is a string 
# print(type(5)) # int
# print(type(5.5)) # float
# print(type(True)) # boolean





# isintance( , ) you pass in a value and a class to see if it is true or false

# a = "hello"
# b = 5
# c = True
# d = 5.2

# print(isinstance(a, str)) #true
# print(isinstance(a, int)) #false
# print(isinstance(c, int)) #true
# print(isinstance(c, float)) #false

# a_string = "1"
# a = "2"

# print(a_string + a) # returns 12 because it is treating them as strings
# print(int(a_string) + int(a)) # returns 3 because you are changing the str to an int
# print(float(a_string) + float(a)) # returns 3.0 because you are changing the str to a float




# # passing multiple arguments into a print function 

# print('one', 'two', 'three') # separate them by commas




# putting in line breaks using escape character
# \n means line break
# \t indents with 5 spaces
# \v puts vertical spacing between lines
# \b puts backspaces 





# Casting = changing one data type to another 
# using int() to change a string or vice versa
# str()  float()  int()  



#input function 

# user_name = input("What is your name?")
# age = input("How old are you?")
# year_of_birth = 2020 - int(age)
# print(f"Thank you, {user_name}")
# print(f"You were born in {year_of_birth}")
# print(type(user_name)) # the datatype returned from input is always going to be a string
#because it always returns strings, use int() or float() in order to use the data returned as a number



# if statements

# if condition:
#     block 
# else:
#     otherwise block 

# age = 23 

# if (age >= 21):
#     print("you are old enough to drink")
# elif (age >= 18 and < 21):
#     print("you're almost old enough, but not quite.")
# else: 

# number = int(input("Give me a number, any number."))

# if number % 2 == 0:
#     print(f"The number you gave me, {number}, is an even number.")
# elif number % 2 == 1:
#     print(f"The number you gave me, {number}, is an odd number.")


# while statements / loops

# count = 0 

# while count < 10:
#     count += 1
#     print(f"The count is {count}")

# print("done with count")

# answer = ""

# while answer != "when":
#     answer = input("say when: ")
#     answer = answer.lower() 

# print("Cheese")



# number = ""

# while number != -1:
#     number = int(input("Give me a number, any number"))
#     if number % 2 == 0:
#         print(f"The number you gave me, {number}, is an even number.")
#     elif number % 2 == 1:
#         print(f"The number you gave me, {number}, is an odd number.")

# print("Zero is not a valid number")

# num = ""
# while num!= -1:
#     num = int(input("Please enter a number: "))
#     if num % 2 == 0:
#         print("This is an even number")
#     elif num == -1:
#         print("exit")
#     else:
#         print("This is an odd number")

















