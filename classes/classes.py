class User:
    def __init__(self,username,email):
        #self refers to the current object.
        self.username=username
        self.email=email
    #function to print username and email
    #Methods are simply functions inside a class.
    def display_info(self):
        print(f"\nUsername: {self.username}")
        print(f"\nEmail: {self.email}")

#create instance of a class
user1=User("bashbytes","bash@gmail.com")
#display results
user1.display_info()
# Username: bashbytes
#Email: bash@gmail.com
user2=User("alex","alex@gmail.com")
#display results
user2.display_info()
#Username: alex
#Email: alex@gmail.com


#Inheritance
#means create a new class using an existing class
#example
#create another class Admin
#which inherits from User class
class Admin(User):
    #extend parent's functionality
    def __init__(self,username,email,role):
        super().__init__(username,email)
        self.role=role
    #function to display details
    def display_details(self):
        print(f"\nUsername: {self.username}\nEmail: {self.email}\nRole: {self.role}")
    


#create an instance of Admin class
admin1=Admin(
    "Bashbytes Imla",
    "bashbytesimla@gmail.com",
    "Super admin"
)
#show results
admin1.display_details()
#Username: Bashbytes Imla
#Email: bashbytesimla@gmail.com
#Role: Super admin


#method overriding
#happens when a child class provide its own version of a method that already exist in the parent class
#example
class User2:
    def login(self):
        print("\nLogin successful")
class Admin2(User2):
    def login(self):
        print("\nLogin successful")
        print("Opening admin panel")
class Moderator(User2):
    def login(self):
        print("\nLogin successful...")
        print("Opening moderation tools\n")


#instance of user1
user_one=User2()
#call login method
user_one.login() #Login successful

#instance of admin 2
admin_two=Admin2()
#call login method
admin_two.login()
#Login successful
#Opening admin panel

#instance of Moderator
moderator=Moderator()
#call login method
moderator.login()
#Login successful...
#Opening moderation tools