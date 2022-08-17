
#? This file is focused on Understanding Tuples 
# TODO: Practice with other examples.. If you get stuck, Google is your friend :)

#? Tuples are used to store multiple items in a single variable.
#? Tuple items are ordered, unchangeable, and allow duplicate values.

#* Simple explanation of a tuple 
from ast import While


tuple_num = (192, 12.8)
print(tuple_num)
tuple_string = ("orange", "apple")
print(tuple_string)

#* tuple length using the len()
tuple_length = ("dog", "cat", "monkey")
print(len(tuple_length))

#* Getting the type of datatype it is 
print(type(tuple_length))

#* accessing tuples 
tuple_access = (2, 5, 7, 8)
print(tuple_access[0])

#* range of  indexes 
print(tuple_access[1:3])

#* checking if tuple exists 
#? using the tuple_access variable created
if 3 in tuple_access:
    print("its in the tuple")
else:
    print("not in tuple")    


#* updating a tuple 
#! Note: tuples can't be changed. 
#ToDO: to change a tuple we'd have to convert it to a list first
tuple_change = ("bathroom", "poolroom", "waitingroom", "kitchen")
tuple_change_list = list(tuple_change)
tuple_change_list.append("sitting room")
tuple_change = tuple(tuple_change_list)
print(tuple_change)


#* looping through a tuple
#? using the for loop
for_tuple = ("poolroom", "waitingroom", "kitchen")
for i in for_tuple:
    print("its in this tuple")


#? using the While loop
while_tuple = ("room1", "room2", "room3")
while "room1"  in while_tuple:
    print("It's in!! ")
    break
      
#* join tuple
#? I will join for_tuple with while_tuple to demonstrate the join tuples
tuple_join =  for_tuple + while_tuple
print(tuple_join)


#* tuple count() method
#? Returns the number of times a specified value occurs in a tuple
tuple_join.count("room2")
