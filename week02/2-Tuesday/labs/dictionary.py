# 1. Create a dictionary called zodiac with the following inforation.
# Each key is the name of the zodiac


# ies - The Warrior
# Taurus - The Builder
# Gemini - The Messenger
# Cancer - The Mother
# Leo - The King
# Virgo -The Analyst
# Libra - The Judge
# Scorpio - The Magician
# Sagittarius - the Gypsy
# Capricorn - the Father
# Aquarius - The ThinkerAr
# Pisces - TheMystic

# zodiac = {
#     "Aries": "The Warrior",
#     "Taurus": "The Builder",
#     "Gemini": "The Messenger",
#     "Cancer": "The Mother",
#     "Leo": "The King",
#     "Virgo": "The Analyst",
#     "Libra": "The Judge",
#     "Scorpio": "The Magician",
#     "Sagittarius": "The Gypsy",
#     "Capricorn": "The Father",
#     "Aquarius": "The ThinkerAr",
#     "Pisces": "TheMystic"

# }

# print(zodiac["Sagittarius"])



# # get() method 

# print(zodiac.get("Scorpio"))

# #if there is not a key that you call, with get() you get None instead of an error 
# print(zodiac.get("cupcake")) #none



# in method checks to see if a key is in a dictionary 

# isValid = "cupcake" in zodiac
# print(isValid) #get False bc it is not in the dictionary 


#update: to push a new value for a key 

# zodiac["Aries"] = "the first sign"
# print(zodiac["Aries"])


# # .keys() and .values() returns an array with either the keys or values 
# # keys = zodiac.keys()
# # print(keys)

# # values = zodiac.values()
# # print(values)


# # Delete del 

# # print(zodiac)
# # del zodiac["Aries"]
# # print(zodiac)

# # ADD
# # zodiac["Aries"] = "The first sign"
# # print(zodiac)

# # 1a. Retrieve information about your zodiac from the zodiac dictionary




# # 2. Given the following dictionary

# # phonebook_dict = {
# #     'Alice': '703-493-1834',
# #     'Bob': '857-384-1234',
# #     'Elizabeth': '484-584-2923'
# # }


# # phonebook_dict["Kareem"] = "938-489-1234"
# # # 2a. Print Elizabeth's phone number
# # print("Elizabeth's number = ", phonebook_dict["Elizabeth"])

# # # 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# # phonebook_dict['Kareem'] = '938-489-1234'
# # print("Kareem's number = ", phonebook_dict["Kareem"])
# # # 2c. Delete Alice's phone entry.
# # del phonebook_dict["Alice"]
# # # 2d. Change Bob's phone number to '968-345-2345'.
# # phonebook_dict['Bob'] = '968-345-2345'
# # # 2e. Print all the phone entries.
# # print(phonebook_dict)



# # ### .items() will create a tuple for each key value pair

# # items = phonebook_dict.items()
# # print(items)

# # #iterating through dictionary 
# # for key, value in phonebook_dict.items():
# #     print(key)
# #     print(value)





# # # 3. Nested dictionaries - you can nest lists or other dictionaries within dictionaries
# #how to retrieve nested objects
# # use an index to refer to the outside items 

# #ramit[0] will give you the first info about Ramit 
# # ramit[0]['interests'] will return movies and tennis


# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#     {
#         'name': 'Jasmine',
#         'email': 'jasmine@yahoo.com',
#         'interests': ['photography', 'tennis']
#         },
#      {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'tv']
#         }
#     ]
# }
# # # 3a. Write a python expression that gets the email address of Ramit.
# email = ramit['email']
# print(email)

# # # 3b. Write a python expression that gets the first of Ramit's interests.
# first_interest = ramit['interests'][0]
# print(first_interest)
# # # 3c. Write a python expression that gets the email address of Jasmine.
# jas_email = ramit['friends'][0]['email']
# print(jas_email)

# # # 3d. Write a python expression that gets the second of Jan's two interests.
# second_interest = ramit['friends'][1]['interests'][1]
# print(second_interest)

# # 4. Letter Summary
# # Write a letter_histogram function that takes a word as its input,
# # and returns a dictionary containing the tally of how many times
# # each letter in the alphabet was used in the word. For example:

# >>>letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}


#
# def histogram(word):
#     count = {}
#     for i in word:
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] += 1
#     return count
# print(histogram("banana"))

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')


# def word_counter(text):
#     text_list = text.split()
#     text_dict = {}
#     for word in text_list:
#         word = word.lower()
#         if word not in text_dict:
#             text_dict[word] = 1
#         elif word in text_dict:
#             text_dict[word] += 1
#     return text_dict

# print(word_counter("I'm so so so so so happy happy happy"))


#phone book = creates a menu need to know how to store things
    