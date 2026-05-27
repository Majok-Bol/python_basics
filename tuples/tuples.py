animals=("dog","cat","cow","donkey")
print("Animals: ",animals)
print("Type: ",type(animals)) #Type:  <class 'tuple'>
#check length
print("Length: ",len(animals)) # Length:  4
other_animals=["horse","camel","sheep"]
print("Initial list: ",type(other_animals)) #Initial list:  <class 'list'>
#using tuple constructor to contruct tuple items
#change list to tuple
animals_list=tuple(other_animals)
#check type of variable
print("Type: ",type(animals_list)) #Type:  <class 'tuple'>
#loop through tuple items
print("\nList of animals: ")
for animal in animals:
    print(animal)
#loop using range
print("\nLoop through using range() and len()")
for number in range(len(animals)):
    print(animals[number])
#unpacking tuple items
(first,second,third,fourth)=animals
print("\nUnpacking tuple items: ") #First animal:  dog
print("First animal: ",first) #Second animal:  cat
print("Second animal: ",second) #Third animal:  cow
print("Fourth animal: ",fourth) #Fourth animal:  donkey

print("Unpacking using asterisk *")
(first_animal,*second_and_third_animal,fourth_animal)=animals
print("First animal: ;",first_animal) #First animal: ; dog
print("Second and third animal: ",second_and_third_animal) #Second and third animal:  ['cat', 'cow']
print("Fourth animal: ",fourth_animal) #Fourth animal:  donkey

#multiply tuples
multiply_animals=animals*3
print("Animals multiplied by 3: ",multiply_animals) #Animals multiplied by 3:  ('dog', 'cat', 'cow', 'donkey', 'dog', 'cat', 'cow', 'donkey', 'dog', 'cat', 'cow', 'donkey')

#check occurrence of tuple item
print("Check occurrence of dog: ",multiply_animals.count("dog")) #Check occurrence of dog:  3
#check index of tuple item
#returns first occurrence
print("Cat position: ",multiply_animals.index("cat")) #Cat position:  1

#add item to tuple
animal=("zebra")
#add zebra to animals tuple
#first convert animals tuple to list
list_of_animals=list(animals)
print("Type: ",type(list_of_animals)) #Type:  <class 'list'>
#add zebra to the list with append() method
list_of_animals.append(animal)
#convert back to tuple
new_tuple=tuple(list_of_animals)
print("New tuple with zebra added: ",new_tuple) # New tuple with zebra added:  ('dog', 'cat', 'cow', 'donkey', 'zebra')
#get type
print("Type: ",type(new_tuple)) #Type:  <class 'tuple'>


#remove tuple item
#change to list
new_list=list(new_tuple)
print("New animal list",new_list) #New animal list ['dog', 'cat', 'cow', 'donkey', 'zebra']
print("Type: ",type(new_list)) #Type:  <class 'list'>
#remove item
new_list.remove("donkey")
#change back to tuple
new_tuple_items=tuple(new_list)
print("New tuple items with donkey removed: ",new_tuple_items) #New tuple items with donkey removed:  ('dog', 'cat', 'cow', 'zebra')

#delete tuple
#it deletes tuple items completely
item_to_delete=animals
print("Item to delete:",item_to_delete)
#delete item
del item_to_delete
print("Deleted item: ",item_to_delete)
#returns error item_to_delete not defined because it has been deleted permanently