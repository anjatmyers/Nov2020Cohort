# we have 3 things in every programming languages: 
# 1. call stack
# 2. execution context
# 3. memory heap

# SEQUENCES: allows us to access data quickly
# takes data types and allows us to structure it in different ways for however you need to access it efficiently
# data structures allow us to store our data more efficiently

#create way to store days of the week 
#shift + option + down arrow will copy lines quickly
# option plus putting cursor over multiple areas will allow you to delete on multiple lines at once

# day1 = "Monday"
# day2 = "Tuesday"
# day3 = "Wednesday"
# day4 = "Thursday"
# day5 = "Friday"
# day6 = "Saturday"
# day7 = "Sunday"
# #lists = use two [] brackets separtated by commas to hold multiple values that can be accessed by counter
# # the values in a list are called items sitting in 'adjacent memory cells' -V
#days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(days)
# print(days[0])

# # lists in python start from 0 
# # 0. Monday
# # 1. Tuesday
# # 2. Wednesday
# # 3. Thursday
# # 4. Friday
# # 5. Saturday
# # 6. Sunday

# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# # len() tells how many items are in the list 
# # lengthOfArray = len(days)
# # print(lengthOfArray)

# #You can change the value at a specific counter 
# days[1] = "Worst Day"
# print(days)
# you can append() concatenate and use extend() method
# puttting a . after the list's name will bring up a list of python's available methods for the array

# append() adds a new item to the end of a list
#however, it will make a list inside of a list if you append one list to the end of another
# use extend() to make a list with additional items instead of nesting another list

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
# print(todos) 
# todos.append("binge watch a show")
# print(todos) # shows the differences
# print(len(todos)) #shows the new counter number
# todos.append("go to sleep")
# print(todos)
# print(len(todos))

# lists make it easy to loop through the list items 
# to loop through thinsgs you always need a counter, a length

# numsArr = [5, 4, 3, 7, 12, 15, 20, 25]

# index = 0 
# while (index < len(numsArr) ):
#     print(f"{index}: {numsArr[index]}")
#     index += 1

# print(len(numsArr))

#Concatenation fix this example 

# a = [a, b, c, e]
# b = [f, g, h , i]

# c = [a] + [b]
# print(c)

# delete items using the index of the item 
# # del nameOfList[indexToBeDeleted]

#numsArr = [5, 4, 3, 7, 12, 15, 20, 25]

# del numsArr[0]
# print(numsArr)

# del numsArr[1:3] #deletes the second and third item but NOT the fourth
# print(numsArr)



# SLICING not mutating original list, it returns a new list 

#numsArr = [5, 4, 3, 7, 12, 15, 20, 25]

# subList = numsArr[1:4] # will make a new list of[4 3 7]

# print(subList)
# print(numsArr)
# just putting the first number will iterate through the end of hte list [3:] goes three through the end


# .insert will mutate the list and insert whatever comes after the index
# numsArr.insert(0, "hello")
# print(numsArr) # you can only put in one index at a time 


#.pop will mutate the list by taking the last element off and returns the last element that it removes

# print(numsArr)
# poppedElement = numsArr.pop()
# print(numsArr)
# print(poppedElement)



#.index will tell you the index of a certain value in the list. Can take an optional range to scan through

# numsArr = [5, 4, 3, 7, 12, 15, 20, 25]

# neededindex = numsArr.index(20) 
# print(neededindex) # returns 6 because 20 is at the 6th index
# will only return the first occurance if there are multiple 

# .copy()
# difference bw passed by value and passed by reference
# passed by value = get a brand new address (simple data types get a new address)
# passed by reference = BUT when you make a copy of an array it doesnt get a new address 
#placing .copy() at the end of your array will pass it by value 
# by default, strings integers and numbers are passed by value and arrays are passed by reference unless you use the copy.() to copy by value

#.clear()
#removes all items from a list 

#.sort()
#sorts the list 


### MATRIX lists within lists

# matrix = [[0,1], [2,3]]
# # to access a specific index, reference the element number first then reference the index within that element (the list within the list is called an element)
# print(matrix[1][0]) #2

#a has four elements
# a = [ [2, 4, 6, 8, 9, 6, 4 ],  
#     [ 1, 3, 5, 7 ],  
#     [ 8, 6, 4, 2 ],  
#     [ 7, 5, 3 ] ] 
# #loop through to print out all the elements  
# outerIndex = 0
# innerIndex = 0

# while outerIndex <  len(a):
#     print(a[outerIndex])
#     while innerIndex < len(a[outerIndex]):
#         print(a[outerIndex][innerIndex])
#         innerIndex += 1
#     innerIndex = 0
#     outerIndex += 1

# len(a[outerIndex] is telling the inner loop to run once for each outter array. Within the first loop it will cycle through each inner array number then go to the outer index. This will only need to happen as there are many outer arrays.)
# the len(a[outerIndex]) gives the length of each inner array a[0] is 7 a[3] is 3
# control + c to kill an infinite loop 


##strings are like lists
# you can access letters in a string like you access indexes in a list 

#alphabet = "abcdefghijklmnopqrstuvwxyz"
# # index = 0
# # while index < len(alphabet):
# #     print(alphabet[index])
# #     index += 1



# ### list  --- is a data type 
# ###converting strings to lists (you have to change strings to lists in order to change individual letters)

# alph_list = list(alphabet)
# #
# print(alph_list)
# print(alphabet)

# ### join --- to rejoin a list back to a string 

# alphjoin = "".join(alph_list) # what is in the "" you can put a space or . or - and it would put this in between each item in the string 
# print(alphjoin)


###  reverse alphabet (could use length -1 if not using built in functions)

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# alph_list = list(alphabet)

# alph_list.reverse()

# #print(alph_list)

# join_alph = "".join(alph_list)
# print(join_alph)


# me trying to do it without the built in functions 
#could start at alphabet[-1] count down to 0 to go backwards 
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alph_list = list(alphabet)

# index = 0 
# for letter in range(26):
#     print(alphabet)




#####Tuple is a list where you can't change the values 

# contants = (3.14, 2.72)

# print(contants[0])
#you cannot change the values once set 
#usually used in math and science with values that do not change 





#range() function range(start, upto, step) upto does not include that number 
# step will be the stepup size (if its 3 it will increase each number by three)
# can use these with loops 

# one_through_ten = list(range(10))
# print(one_through_ten)

# count_by_3 = list(range(0, 35, 3))
# print(count_by_3)

#### for loop can loop through any type of sequence (tupel, list, string,)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alph_list = list(alphabet)

# for letter in alph_list:
#     print(letter)



#easier way to write the mult table 

# for outter in range(1, 11):
#     for inner in range(10):
#         print(f"{outter} X {inner} = {outter * inner}")