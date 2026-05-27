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