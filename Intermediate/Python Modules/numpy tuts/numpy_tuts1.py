'''
This file we will see some basic stuff  with numpy... eg: >>Accessing arrays, >>dimensions etc
'''
#? Numpy arrays
import numpy as np

#* to check the version of your numpy module (on the terminal write numpy --version) or
print(np.__version__)

#* Creating a one dimensional array
arr_one = np.array([1, 2, 3, 4, 5])
calc = arr_one * 2 
print(calc)

#* Arrang 
my_arr = np.arange(8)
print('Number of elements in array ' + str(my_arr))

#* datatype 
print('datatype ' + str(arr_one.dtype))

#* shape 
print('shape is ' + str(arr_one.shape))

#* reshape
print('reshape ' + str(arr_one.reshape))

#* dimension
print('dimension is ' + str(arr_one.ndim))
#! This is a one dimensional array

#* size
print('size is ' + str(arr_one.size))


#* Two dimensional array
arr_two = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])

#* dimension
print('dimension is ' + str(arr_two.ndim))
#! This is a two dimensional array


#* Two dimensional array
arr_three = np.array([[[1, 2, 3, 4], [2, 4, 6, 8]]])

#* dimension
print('dimension is ' + str(arr_three.ndim))
#! This is a three dimensional array


#*? Accessing arrays 

#* accessing 1 dimensional array
access_arr = np.array([10, 21, 82, 63])
print('one dimentional array ' + str(access_arr[2]))

#* accessing arrays and adding them
print('adding one dimentional array ' + str(access_arr[1] + access_arr[0]))


#* accessing 2 dimentional arrays
two_dimensional_arr = np.array([[22, 33, 45, 88, 22], [20, 52, 43, 45, 98]])  #! Note that the two-dimensional arrays must conatin the same amount of values in each.. 
print('accessing 2 dimentional arrays ' + str(two_dimensional_arr[1,3])) #todo: How it works: look at it as a table with rows and columns.. here row represents the dimension and the index represents the colummn.

#* accessing 3 dimensional arrays
three_dimensional_arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11, 12]]])
print('accessing 3 dimentional arrays ' + str(three_dimensional_arr[0,1,2]))