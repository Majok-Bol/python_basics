fruits={"apple","banana","cherry"}
print("Fruits: ",fruits) #Fruits:  {'banana', 'cherry', 'apple'}
print("Data type: ",type(fruits)) #Data type:  <class 'set'>

#add mango to the set
fruits.add("mango")
print("Fruits: ",fruits) #Fruits:  {'banana', 'cherry', 'mango', 'apple'}

#remove cherry
fruits.remove("cherry")
print('Fruits: ',fruits)

second_fruits_items={"pineapple","watermelon","apple"}
print("Second fruits items",second_fruits_items)
#combine sets using | operator
print(fruits| second_fruits_items) #{'banana', 'mango', 'apple', 'watermelon', 'pineapple', 'cherry'}
third_fruits_items={"apple","pears","guava"}
print("Third fruits items: ",third_fruits_items)
#check common items in second and third sets
common_items=(second_fruits_items & third_fruits_items)
print("Common items: ",common_items) #Common items:  {'apple'}

#check different items in a set
different_items=second_fruits_items-third_fruits_items
print("Different items in second and third sets: ",different_items) #Different items in second and third sets:  {'watermelon', 'pineapple'}

#copy set items
fruits_copy=fruits.copy()
print("Fruits copy: ",fruits_copy) #Fruits copy:  {'banana', 'mango', 'cherry', 'apple'}


#isdisjoint() returns whether two sets have  one or more interesection or not
#True  if two sets have NO common elements
# False if they share at least one common element
check_intersection=second_fruits_items.isdisjoint(third_fruits_items)
print(check_intersection) #False


#issubset() returns true whether another set contains this set or not
#checks if all elements of one set exist inside another set.
check_subset=second_fruits_items.issubset(third_fruits_items)
print(check_subset)#False

#issuperset()
#checks if one set contains all elements of another set.
check_all_elements_exists=second_fruits_items.issuperset(third_fruits_items) #False