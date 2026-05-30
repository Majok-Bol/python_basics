#python functions
#function to print name
def print_name(my_name):
    print(f"My name is: {my_name}")

#call the function
print_name("Henry Ford") #My name is: Henry Ford
print_name("Napoleon Hill") #My name is: Napoleon Hill
print_name("Dale Carnegie") #My name is: Dale Carnegie

#parameter-is a variable listed inside the parenthesis in the function definition eg my_name above
#argument-is a value that is sent to the function when it is called eg ("Henry Ford"),("Napoleon Hill"),and ("Dale Carnegie") above

#*args accepts any number of positional arguments
def add(*args):
    print(args)

add(10, 20, 30, 40) #(10, 20, 30, 40)
add(34,56,78,68) #(34, 56, 78, 68)
add(23,34,56,78,12,34,34,"apple","banana") #(23, 34, 56, 78, 12, 34, 34, 'apple', 'banana')



#Arbitrary keyword arguments(**kwargs)
#**kwargs allows a function to accept any number of keyword arguments
#example
def person(**kwargs):
    #Inside the function, kwargs is a dictionary:
    #print kwargs
    print(kwargs)
    #get the data type
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key}: {value}")

#call the function
person(name="Alex Jones",age=35,country="USA")
'''{'name': 'Alex Jones', 'age': 35, 'country': 'USA'}
<class 'dict'>
name: Alex Jones
age: 35
country: USA'''
person(name="Mary",age=23,gender="Female",country="Russia",hobby="Swimming")
'''{'name': 'Mary', 'age': 23, 'gender': 'Female', 'country': 'Russia', 'hobby': 'Swimming'}
<class 'dict'>
name: Mary
age: 23
gender: Female
country: Russia
hobby: Swimming'''

#use case for arbitrary keyword arguments
#configuration settings
def connect_db(**settings):
    #print settings
    print(settings)
    #get data type
    print(type(settings))
    for key,value in settings.items():
        print(f"{key}:{value}")

#call the function
connect_db(host="localhost",port=3306,user="root")
'''{'host': 'localhost', 'port': 3306, 'user': 'root'}
<class 'dict'>
host:localhost
port:3306
user:root'''



#position only arguments
def divide(first_number,second_number,/):
    return first_number/second_number
#call the function
print(divide(30,6)) # 5.0
#calling the function in this format fails
# #throws error
# print(divide(first_number=34,second_number=2)) # TypeError: divide() got some positional-only arguments passed as keyword arguments: 'first_number, second_number'

#keyword only arguments(*)
def greet(*,name,age):
    print(name,age)
#call the function
greet(name="John",age=35) # John 35
#invalid function call specified as keyword only arguments
# greet("John",35) # TypeError: greet() takes 0 positional arguments but 2 were given


#lambda function
#syntax
# lambda=arguments: expression
#example
x=lambda a:a+10
print(x(20)) # 30

#other example
check=lambda age:"Adult" if age>=18 else "Minor"

#call function
print(check(39)) #Adult
print(check(9)) #Minor
print(check(17)) #Minor