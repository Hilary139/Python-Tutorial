
#? Dictionaries are used to store data values in key:value pairs.
#?A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

'''

#* Dictionary example 
dict_profile = {
    "name": "Kingsley",
    "age": 28,
    "weight": 1,
    "complection": "dark",
    "language": "English"
}
print(dict_profile)

#* dictionary items
print(dict_profile["age"])
print(dict_profile["weight"])


#* dictionary key
#!Dictionaries cannot have two items with the same key:
dict_profile_update = {
    "name": "Kingsley",
    "age": 28,
    "weight": 1,
    "complection": "dark",
    "language": "English",
    "age": 33
}
print(dict_profile_update)


#* dictionary type and length
print(type(dict_profile_update))
print(len(dict_profile_update))


#* getting dictioanry key using the key() function
keys = dict_profile_update.keys()
print(keys)

#* getting the values using the values() function
values = dict_profile_update.values()
print(values)


#* The items() method will return each item in a dictionary, as tuples in a list.
dictionary = dict_profile_update.items()
print(dictionary)

#* checking if key exists
if "weight" in dict_profile_update:
    print(dict_profile_update["weight"])
else:
    print("No such key")    


#* changing the value of the key 
dict_profile_update["weight"] = 2.0
dict_profile_update["age"] = 33


#* update the dictioanry using update() function
dict_profile_update.update({"language": "Spanish"})

#* addding an item to the dictionary
dict_profile_update['Height'] = 30

#* removing an item 
dict_profile_update.pop('Height') #! Removes the height from the dictionary
dict_profile_update.popitem() #!The popitem() method removes the last inserted item
del dict_profile_update["age"] #!The del keyword removes the item with the specified key name:
dict_profile_update.clear() #! The clear() method empties the dictionary:


#* looping through a dictionary
for y in dict_profile_update:
    print(y) #! prints all the keys one by one

for y in dict_profile_update:
    print(dict_profile_update[y]) #! prints all the values one by one


#* loopimg through keys
for y in dict_profile_update.keys():
    print(y)

#* looping through values
for y in dict_profile_update.values():
    print(y)

#* looping through items 
for y in dict_profile_update.items():
    print(y)    


#* Make a copy of a dictionary with the copy() method:
dict_profile_copy = dict_profile_update.copy()
print(dict_profile_copy)

#* nested dictionary
school_students = {
    "name": "Daniel",
    "age": 20
},
{
    "name": "james",
    "age": 21
},
{
    "name": "john",
    "age": 22
}

#? We can also create Duifferent single dictionaries and add them together in a single dictionary.. example below
dict_one = {
    "language": "English",
    "other language": "French"
}

dict_two = {
    "country": "Canada"
}

dict_three = {
    "continent": "North america"
}

combiined_dict = {
    "languages" : dict_one,
    "country": dict_two,
    "continent": dict_three
}

print(combiined_dict)


#? Dictionary Methods
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''