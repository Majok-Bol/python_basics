
#dictionaries are key-value pairs dataset
first_fruit={
    "name":"Mango",
    "price":30,
    "is_ripe":True
  
}
print("First fruit: ",first_fruit) #First fruit:  {'name': 'Mango', 'price': 30, 'is_ripe': True}
print("Data type: ",type(first_fruit))  #Data type:  <class 'dict'>

second_fruit={
    "name":"Pineapple",
    "price":35,
    "is_ripe":False
  
}

print("Second fruit: ",second_fruit) #Second fruit:  {'name': 'Pineapple', 'price': 35, 'is_ripe': False}
#return keys
print(first_fruit.keys()) #dict_keys(['name', 'price', 'is_ripe'])
#return values
print(first_fruit.values()) #dict_values(['Mango', 30, True])

#changed first fruit price from 30 to 45
first_fruit.update({"price":45})
print("First fruit with price changed: ",first_fruit) #First fruit with price changed:  {'name': 'Mango', 'price': 45, 'is_ripe': True}

#add color to first fruit
first_fruit.update({"color":"green"})
print("First fruit with color added: ",first_fruit) #First fruit with color added:  {'name': 'Mango', 'price': 45, 'is_ripe': True, 'color': 'green'}


#return items in a dictionary as tuples in a list
print(first_fruit.items())

#check if keyword exists
if "price" in first_fruit:
    print("'Yes,price key exists'") #'Yes,price key exists'



#loop through first frut items
for key,value in first_fruit.items():
    print(f"{key}: {value}")

#remove specified key name  item in a  dictionary 
#it provides default value
#returns its value
#delete second fruit items price key
print(second_fruit.pop("price","Not found")) # 35



#popitem() removes last added item
#remove last added item to second fruits 
print("Removed key-value pair: ",second_fruit.popitem())
# print("Second fruits items: ",second_fruit)

#copy dictionary items
fruits_copy=first_fruit.copy()
print("Fruits copy: ",fruits_copy)

#clear method
#removes all items but keeps dictionary itself
#clear second_fruits
second_fruit.clear()
print("Now empty: ",second_fruit)
