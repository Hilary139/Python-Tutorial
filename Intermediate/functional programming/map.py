
#* Map takes a function and a collection of items.
list_map = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#* Using lamda function with maps function
map_list_result = map(lambda x: x*2, list_map) #? This function multiplies 2 with the list. 
print(list(map_list_result)) #* This function multiplies 2 with the list and displays the result.


map_fruits = ["Apple", "Orange", "Grape", "Mango", "Pear"]

#* Using lamda function with maps function
map_fruits_result = map(lambda fruits: fruits.upper(), map_fruits) #? This function makes all the fruits in capital letters
print(list(map_fruits_result)) #* This function returns a list of fruit names all in capital letters



#todo: Notice that map() function ilterates the list of fruit names and the list of numbers and performs actions accordingly.



#! Note: yYou can decide to return the results either in sets, list or tuple instead.
#print(list(map_fruits_result)) #* This returns it inform of a list..
#print(set(map_fruits_result)) #* This returns it inform of a set..
#print(tuple(map_fruits_result)) #* This returns it inform of a tuple..

def test():
    list_box = []
    for x in map_fruits:
        list_box.append(x.upper())
        print(list_box) 

test()        
