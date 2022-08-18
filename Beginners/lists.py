
#? This is a summary of list and how you can maipulate lists 
# TODO: Practice with other examples.. If you get stuck, Google is your friend :)

#? Lists are used to store multiple items in a single variable.

house = ["bedroom", "bathroom", "poolhouse", "garage", "dinning", "playground"]
print(house)

house_measurements = [["bedroom", 1.44], ["bathroom", 1.09], ["poolhouse", 2.33], ["garage", 2.00], ["dinning", 1.50], ["playground", 3.88]]
print(house_measurements)


#! Note: Not all the list functiions were used in this example

#* slicing lists
house_measurements_fill = house[:2]
house_measurements_down = house[3:5]
print(house_measurements_fill)
print(house_measurements_down)


#* math functions
height = max(house_measurements)
print(height)

#* accessing lists (positive idexing)
print(house_measurements[4])
print(house_measurements[5])

#* accessing lists (negative indexing)
print(house[-2])
print(house[-1])

#* changing lists 
house_measurements[4] = ["store room", 2.46]
print(house_measurements) 


#* adding to lists
house.append("basement")
print(house)

#* removing from a list 
house.remove("basement")
print(house)

#* working withh pop(), del() and clear()
testiing_list = ["a", "b", "c", "d", "e", "f"]

#? functions 
#* pop()
testiing_list.pop() #! this removes the last item from the list
print(testiing_list)

#* del()
del testiing_list[0] #! this removes the first item from the list
print(testiing_list)

#* clear()
testiing_list.clear() #! this removes all the items from the list  
#? End 


#* Sorting lists 
sort_list = [2, 1, 5, 6, 6, 7, 4]
sort_list.sort() #! this sorts the list in acending order
print(sort_list)

sort_list.reverse() #! this sorts the list in decending order
print(sort_list)


#? There are different ways of copying a list
#* list copying Method one:
copy_list = house_measurements.copy()
print(copy_list)

#* second method:
copy_list_two = list(house)
print(copy_list_two)

#TODO Pracice more of this with other examples of your choice. Google is your Friend :)

#* Joinig lists
list_join  = [3, 5, 6, 7]
list_join_extention = [2, 4, 8]
list_join.extend(list_join_extention)

#? Another easy way to join list is to use the + operator
list_one = [1, 2, 3]
list_two = [4, 5, 6]
list_join_result = list_one + list_two 
print(list_join_result)



#* looping lists
#* Using FOR LOOP 
for i in house_measurements:
    #* Adding condition to the loop
    if house_measurements[3] in house:
        print(i)
    else: 
        print("not found")    


#* Using WHILE LOOP
i = 0 
while i < len(house_measurements):
    #* adding condition in the loop
    if house_measurements[3] in house:
        print(house_measurements[3])
        i += 1
    else:
        print("Opps!!")
        i += 1 
# TODO: PRACTICE more of the above examples... :)


#? Other List methods
#TODO: Always practice!!! :)
'''
        append()	Adds an element at the end of the list
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	Returns the index of the first element with the specified value
        insert()	Adds an element at the specified position
        pop()	Removes the element at the specified position
        remove()	Removes the item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list
        
'''

