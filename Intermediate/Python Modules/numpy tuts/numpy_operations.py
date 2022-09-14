
''' Working with numpy operations'''

import numpy as np
a = np.zeros((3,3))
a[:] = 4 #? Making all elements to be 4 in the array
print('Assigning 4 to the all elemets in the array\n '+ str(a))

#* Using fill method
b = np.zeros((2,2))
b[:] = 3
b.fill(6)
print('filling the array with 6\n ' + str(b))
print('\n')

#* OPERATORS 
#? We can add, subtract, and multiply values in our array using operators
'''
Example: 
b += 2 # This will add 2 to all values in the array
'''
# Arthmetic methods
#* Sum() >> Sum
c = np.zeros((2,2))
c.fill(5)
arr_sum = c.sum() # This would add the entire array and give you an output
print(c)
print('sum of this array is ' + str(arr_sum))

#todo To access each of the row... Add 1 to the parentheses
# arr_sum = c.sum(1)
#todo To access each of the column... Add 0 to the parentheses
# arr_sum = c.sum(0)

#* prod() >> Product 
d = np.zeros((3,3))
d.fill(4)
arr_product = d.prod()
print(d)
print('Product of this array is ' + str(arr_product))


#* Getting the mean >> mean()
array_average = d.mean()
print('The average of this array is ' + str(array_average))

#* Finfing minimum and maximum values
e = np.array([[30,22],[30,50],[20,10]])
array_maximum = e.max()
print('The maximum value of this array is ' + str(array_maximum))

array_minimum = e.min()
print('The minimum value of this array is ' + str(array_minimum))

#* Getting the index 
# using argmax() and argmin()
array_arg_maximum = e.argmax()
print('The index maximum value of this array is ' + str(array_arg_maximum))

array_arg_minimum = e.argmin()
print('The index minimum value of this array is ' + str(array_arg_minimum))

#* p2p >> Peak-to-Peak
peak_to_peak = e.ptp()
print('The peak value of this array is ' + str(peak_to_peak))
#!peak to peak means max() - min()

#* Flatten the array
array_flat = e.flatten() #! this changes the dimension of the array i.e 2 dimension to 1 dimension
# array_flat = e.reshape(e.size) #?Another way to flatten the array
# array_flat = e.ravel() #?Another way to flatten the array
print('Flattening the array '+ str(array_flat))

#* repeat values/array
array_repeat = np.repeat(333,4)
print('Repeating values/array '+ str(array_repeat))

#todo: Note: 1 is rows and 0 is columns
f = np.array([[2,3],[4,5]])
array_repeat_arrange = np.repeat(f,3,axis=0)
print('Repeating values/array and arranging it by colunm '+ str(array_repeat_arrange))

f = np.array([[2,3],[4,5]])
array_repeat_arrange = np.repeat(f,3,axis=1)
print('Repeating values/array and arranging it by row '+ str(array_repeat_arrange))

#* Making the arrays unique
array_unique = np.unique(array_repeat_arrange, axis=1)
print('Making unique arrays ' + str(array_unique))

#* diagonal
array_diagonal = np.diagonal(array_repeat_arrange)
print('diagonal arrays ' + str(array_diagonal))


#* Conversion and storage 
# Converting my numpy array to a python list
'''
array_convert = np.array([[1, 2, 3] [4, 5, 6]])
array_convert_type = array_convert.astype('integer')
array_convert_to_list = array_convert_type.tolist()
print('converted numpy array to list ' + str(array_convert_to_list)) 
print('checking the datatype of the array ' + type(array_convert_to_list))
'''
#* store the array in to a file
store_array = f.tofile("my_array.txt", sep=',')  #! this will automatically create a new file "my_array.txt" in your directory


#* transposition >> swapping the array i.e row values would be column values and vice versa
array_swapped = np.swapaxes(f,1,0)
# or: f.transpose() #? this would swap it as well
# or: f.T (Using a single attribute )which is called Transposed.
print('Swapped the row values to column values '+ str(array_swapped))




#TODO: There are more numpy functions that are not covered here.. You can checkout the doumentation (https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to find more