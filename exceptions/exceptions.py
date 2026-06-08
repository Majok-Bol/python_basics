#manage errors that arise during program execution
#try....except blocks
try:
    user_input=int(input("Enter a number: "))
    print(f"You entered: {user_input}")
except:
    print("That is not a valid number") #That is not a valid number




#catch specific error
try:
    result=10/0
except ZeroDivisionError:
    print("You cant divide by 0") #You cant divide by 0


#getting the error message
try:
    num1=int("abc")
except ValueError as e:
    print("Error occurred: ",e) # Error occurred:  invalid literal for int() with base 10: 'abc'




#additional notes
'''
ZeroDivisionError:  Dividing by zero
ValueErrorWrong:    type of value (e.g. int("abc"))
TypeError:          wrong data type in operation
FileNotFoundError:   Opening a file that doesn't exist
IndexError:           Accessing a list index that doesn't exist
'''


#finally...always runs whether error occurred or not
#read file
try:
    my_file=open("data.txt","r")
    content=my_file.read()
    #print contents
    print(f"File contents: \n{content}")
    '''
File contents: 
Welcome to Python basics tutorial.
Python is beginner friendly.
Python is open source.
    '''
except FileNotFoundError as e:
    print("Error: ",e)
finally:
    print("This always runs-good for closing files") #This always runs-good for closing files
