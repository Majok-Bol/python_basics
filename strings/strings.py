'''strings in python are arrrays representing unicode characters'''
#example
my_name="Henry Ford"
print("My name is : ",my_name) #My name is: Henry Ford
#type of variable
print("Type: ",type(my_name)) #Type:  <class 'str'>
#looping through a string
for character in my_name:
    print(character)

#check string length
print(len(my_name)) #10

#checking if a string exists
#check if string 'Ford' exists in my_name variable
print("Ford" in my_name) #True

#check if string does not exist
print("Jane" not in my_name) #True

#slicing strings
#slices upto the 9th character
print(my_name[:9]) #output Henry For
#slices from 3rd character upto 8th character,9th character not included
print(my_name[3:9]) #ry For
#slices from 2nd character upto the end
print(my_name[2:]) #nry Ford


#convert to uppercase
upper_case=my_name.upper()
print("Upper case: ",upper_case)
#convert to lowercase
lower_case=my_name.lower()
print("Lower case: ",lower_case)

#removing whitespaces
spaced_characters="  My name is Henry Ford   "
print("Spaced characters: ",spaced_characters)
remove_white_space=spaced_characters.strip()
print("Removed white spaces: ",remove_white_space)

#remove left white spaces
left_space=spaced_characters.lstrip()
print("Left spaces removed: ",left_space)
#remove right white spaces
right_space=spaced_characters.rstrip()
print("Right white spaces removed: ",right_space)


#replace characters
replaced_characters=spaced_characters.replace("F","N")
print(replaced_characters)
#split characters at white spaces
split_characters=my_name.split(" ")
print("Split characters: ",split_characters) #['Henry', 'Ford']

#check if number is a digit
my_number="1000"
print("Check if number: ",my_number.isdigit()) #True
#check if it is a string
my_string="Python"
print(isinstance(my_string,str)) # True


#find position of a character
position=my_name.find("Ford") 
print("Position: ",position)# found in 6th position
#check if sentence end with specific character
print(my_name.endswith("d"))#True
#check if sentence start with specific character
print(my_name.startswith("H")) #True
#check occurrence of a string
fruits="apple,banana,apple,orange"
#check occurrence of apple in fruits variable
print(fruits.count("apple")) # 2
num1=100000
#use comma as a separator
formatted_number=f"{num1:,}"
print("Comma separated number: ",formatted_number) #100,000
#if the number is a string
number="1000000000"
#convert to int first
formatted="{:,}".format(int(number))
print(formatted) #1,000,000,000