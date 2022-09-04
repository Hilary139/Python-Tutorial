
#* Filter takes a function and a collection. It returns a collection of every item for which the function returned True.

#* Example: filter
num = [5, 10, 25, 30, 45, 50, 65, 70, 80, 90, 100] # list of numbers to filter

filter_num = filter(lambda x : x > 50, num) #* This function returns a list of numbers greater than 50. The filter() filters the list to return the result.
filter_num_two = filter(lambda y : y < 50, num) #* This function returns a list of numbers less than 50
print(list(filter_num)) #* This returns it inform of a list..
print(list(filter_num_two)) 


#! Note: yYou can decide to return the results either in sets, list or tuple instead.
#print(list(filter_num)) #* This returns it inform of a list..
#print(set(filter_num)) #* This returns it inform of a set..
#print(tuple(filter_num)) #* This returns it inform of a tuple..



#* this performs the same thing as the filter function.
#using the regular function.
def test() :
    set_num =[]
    for x in num :
        if x > 50:
           set_num.append(x)
        print(set_num)

test()        