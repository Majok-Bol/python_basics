fruits=["apple","banana","cherry","orange","mango","pineapple","straberry","guava"]
print("Fruits: ",fruits)
#get length of fruits variable
print("Length: ",len(fruits)) # 8 
#loop through fruits list
for fruit in fruits:
    print(fruit)
#slicing at specified character
#slice upto the 3rd character
print(fruits[:3])
#check if fruit exists
if "apple" in fruits:
    print("'Yes,apple exists in the list'") #'Yes,apple exists in the list'
#check fruit
#change apple to watermelon
fruits[0]="Watermelon"
print(fruits) #['Watermelon', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava']
#insert at specified position
#add pears at position 2
fruits.insert(2,"Pears")
print(fruits) #['Watermelon', 'banana', 'Pears', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava']
#add Pawpaw to the end of the list
fruits.append("Pawpaw")
print(fruits) #['Watermelon', 'banana', 'Pears', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava', 'Pawpaw']


other_fruits=["Lemon","Passion"]
print("Other fruits list: ",other_fruits) #Other fruits list:  ['Lemon', 'Passion']
#combine fruits list with other_fruits list
fruits.extend(other_fruits)
print("New combined fruits list: ",fruits) 
#New combined fruits list:  ['Watermelon', 'banana', 'Pears', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava', 'Pawpaw', 'Lemon', 'Passion']


#list comprehension
[print(fruit) for fruit in fruits] #prints whole list

#copy list
list_copy=fruits.copy()
print("List copy: ",list_copy)
 #List copy:  ['Watermelon', 'banana', 'Pears', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava', 'Pawpaw', 'Lemon', 'Passion']
 #count occurrence of list item
apple_list=["apple","apple","apple"]
#add three more apples to fruits list
fruits.extend(apple_list)
print("Apple occurrence: ",fruits.count("apple")) # 3

#sort list items
print("Unsorted fruits: ",fruits) #Unsorted fruits:  ['Watermelon', 'banana', 'Pears', 'cherry', 'orange', 'mango', 'pineapple', 'straberry', 'guava', 'Pawpaw', 'Lemon', 'Passion', 'apple', 'apple', 'apple']
#by default sort sorts fruits in ascending order
#sort in ascending order
fruits.sort()
print("Fruits sorted in ascending order: ",fruits) #Fruits sorted in ascending order:  ['Lemon', 'Passion', 'Pawpaw', 'Pears', 'Watermelon', 'apple', 'apple', 'apple', 'banana', 'cherry', 'guava', 'mango', 'orange', 'pineapple', 'straberry']
#sort in descending order
fruits.sort(reverse=True)
print("Sorted in descending order: ",fruits) #Sorted in descending order:  ['straberry', 'pineapple', 'orange', 'mango', 'guava', 'cherry', 'banana', 'apple', 'apple', 'apple', 'Watermelon', 'Pears', 'Pawpaw', 'Passion', 'Lemon']
#return index of specified item
apple_index=fruits.index("apple")
print("Apple index: ",apple_index) #Apple index:  7