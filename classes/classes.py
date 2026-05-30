class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
        #function to print username and email
    def display_info(self):
        print(f"\nUsername: {self.username}")
        print(f"\nEmail: {self.email}")

#create instance of a class
user1=User("bashbytes","bash@gmail.com")
#display results
user1.display_info()
user2=User("alex","alex@gmail.com")
#display results
user2.display_info()