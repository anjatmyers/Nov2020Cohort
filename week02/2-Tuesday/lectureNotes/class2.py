# file_handle = open("hello.txt", 'w')

# file_handle.write("hello world\nthis is a new line")

# file_handle.close()

# file_handle = open('declaration.txt', 'r')

# contents = file_handle.read()

# file_handle.close()

# print(contents)

#### apend a file 
# ...read slides to see how you do this 


### preventing memory leaks
# with open('hello.txt', 'r') as file_handle:
#     contents = file_handle.read()
# ## the with is a context manager 



###pickling 
#allows us to save objects in a dictionary format 

# import pickle
# data = {'name': 'Paul'}
# with open('data.pickle', 'wb') as fh:
#   pickle.dump(data, fh)
 ### dumping to a file, writing it 'wb'

import pickle

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
    {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
     {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}

with open('ramit.pickle', 'wb') as fx:
    pickle.dump(ramit, fx)


#### 
with open('ramit.pickle', 'rb') as fh:
    phonebook = pickle.load(fh)
### this assigns the contents of that dictionary to a variable that you can reference throughout because it is a global variable 


print(phonebook['friends'])