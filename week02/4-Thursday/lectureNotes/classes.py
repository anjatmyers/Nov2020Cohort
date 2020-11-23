# class Person:
#     def __init__(self, name, lastName, birthdate, address, telephone, email):
#         self.name = name
#         self.lastName = lastName
#         self.birthdate = birthdate
#         self.address = address 
#         self.telephone = telephone
#         self.email = email
#         self.friends = []

#     def print_contact_info(self):
#         print(f"Contact {self.name} here:\nphone:{self.telephone} email:{self.email}")

#     def add_friend(self, friend):
#         self.friends.append(friend)
#         return self.friends
    
#     def num_friends(self):
#         print(f"{self.name} has {len(self.friends)} friends")
#         print("Here are their names:")
#         for friend in self.friends:
#             print(f'{friend.name} {friend.lastName}')
#         return len(self.friends)

# ## composition will help manage all the objects - uses one class to manage all other classes
# class Campus:
#     def __init__(self):
#         self.students = []
#     def add_student(self, name, lastName, birthdate, address, telephone, email):
#         student = Person(name, lastName, birthdate, address, telephone, email)
#         self.student.append(student)

#     def current_students(self):
#         for studentObj in self.students:
#             print(f'{studentObj.first} {studentObj.lastName} {studentObj.email}')

# dc = Campus()

# dc.add_student('Sonny', 'Jones', '11/19/2000', '123 sesame st', 'sonny@hotmail.com', '123-456-6789')
# dc.add_student('Jordan', 'Roberts', '5/18/2000', '155 sesame st','jordan_@aol.com', '987-654-3245')

# dc.current_students()
# # sonny = Person('Sonny', 'Jones', '11/19/2000', '123 sesame st', 'sonny@hotmail.com', '123-456-6789')
# # jordan = Person('Jordan', 'Roberts', '5/18/2000', '155 sesame st','jordan_@aol.com', '987-654-3245')
# susan = Person('Susan', 'Black', '8/23/1999', '200 sesame st','susie_q@aol.com', '984-777-3111')
# valerie = Person('Val', 'Conrad', '2/4/1997', '200 sesame st','val_gal@aol.com', '984-767-9999')

# sonny.add_friend(sonny)
# sonny.add_friend(susan)
# sonny.add_friend(valerie)
# sonny.add_friend(sonny) # #beyourownfriend

# sonny.num_friends()
# jordan.num_friends()
# no friends for jordan
# sonny's the coolest

# print("Want to be Sonny's friend too?")
# sonny.print_contact_info()




##### Bank account example

class AccountHolder:
    def __init__(self, fName, accountType, status, balance):
        self.fName = fName
        self.accountType = accountType
        self.status = status
        self.balance = balance
        


class Bank:
    def __init__(self, company, address):
        self.company = company
        self.address = address
        self.accounts = []

    def openAccount(self, fName, accountType, status, balance):
        newAccount = AccountHolder(fName, accountType, status, balance)
        self.accounts.append(newAccount)
    
    def show_account_holders(self):
        for person in self.accounts:
            return person.fName
        # return name, status, and balance

    def show_bank_balance(self):
        bank_balance = 0 
        for person in self.account:
            bank_balance += person.balance
        return bank_balance
        # Layne's work: 
        # def show_bank_balance(self):
        # total_balance = 0
        # for ele in self.accounts:
        #     total_balance += ele.balance
        # return total_balance



    
wells_fargo1 = Bank('Wells Fargo', '123 Main St')

wells_fargo1.openAccount('Andrea', 'Checking', 'Active', 500)
print(wells_fargo1.show_account_holders())


