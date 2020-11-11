# school = "Digital Crafts"
# print(school)

#quick copy of lines of code = shift + option + down arrow
# command + forward slash to comment out blocks of code
 
# string formating 

student1 = "Andrea"
student2 = "Zach"
student3 = "Michael"
student4 = "Rick"

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

# f strings = f stands for format (this way is quicker)
day = "Wednesday"
tomorrow = "Thursday"

# f"Today is {day}" this is a string

current_day = f"Today is {day}"
next_day = f"Tomorrow is {tomorrow}"

print(current_day)
print(next_day)