
#* Reduce takes a function and a collection of items. It returns a value that is created by combining the items
from functools import reduce  #! you'd have to call reduce function from the "functools" package

#* example: reduce function
reduce_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#* using reduce function to add all values in the list..
reduce_list_result = reduce(lambda x, list: x+list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(reduce_list_result)



