'''strings in python are arrrays representing unicode characters'''
#example
my_name="Henry Ford"
print("My name is : ",my_name) #output is My name is: Henry Ford
#looping through a string
for character in my_name:
    print(character)

#check string length
print(len(my_name)) #output 10

#checking if a string exists
#check if string 'Ford' exists in my_name variable
print("Ford" in my_name) #output True

#check if string does not exist
print("Jane" not in my_name) #output True

#slicing strings
#slices upto the 9th character
print(my_name[:9]) #output Henry For
#slices from 3rd character upto 8th character,9th character not included
print(my_name[3:9])
#slices from 2nd character upto the end
print(my_name[2:])


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
print(split_characters)

#check if number is a digit
my_number="1000"
print(my_number.isdigit())
#check if it is a string
my_string="Python"
print(isinstance(my_string,str)) # True


#find position of a character
position=my_name.find("Ford") 
print(position)# found in 6th position
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
print("Comma separated number: ",formatted_number)
#if the number is a string
number="1000000000"
#convert to int first
formatted="{:,}".format(int(number))
print(formatted)