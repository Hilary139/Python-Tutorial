
#todo: This file touches >> slicing arrays, >> datatypes, >> copy and view functions

#* numpy array slicing
import numpy as np 
#? Slicing means taking elements from one given index to another.

'''
we can define it like this: [start : end] or [start : end : step]

'''

#* examples 
slice_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print('slice from 1:5 ' + str(slice_arr[1:5])) #! Note it dose not add the last element. 

#? start from the beginning to the a specific end point
print('slice from beginning to 6 ' + str(slice_arr[:6])) #? or [0:6]

#? start from a specific point to end
print('slice from 2 to end ' + str(slice_arr[1:])) 

#* Negative slicing
slice_arr_neg = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20])
print('slice from end to 15 ' + str(slice_arr_neg[-6:]))


#* Steps: values to determine the step of the slicing
print('return every other element from index 1 to 4 ' + str(slice_arr_neg[1:4:2]))






#? datatypes in numpy arrays
'''
        i >> integer
        b >> boolean
        u >> unsigned integer
        f >> floating point
        c >> complex
        m >> timedelta
        M >> datatime
        O >> object
        S >> string
        u >> unicode string
        v >> fixed chunk of memmory for other types (void)
'''
#*  to check datatype 
arr = np.array([1, 2, 3, 4, 5])
print('to check datatype ' + str(arr.dtype))

#* Creating array with a defined data type 
arr_string = np.array([51, 42, 33, 24, 15] , dtype='S')
print('list the array which is string ' + str(arr_string))
print('chck the datatype which would be string ' + str(arr_string.dtype))
#todo: You can try it out with other datatypes listed above





#* converting a datatype
convert_arr = np.array([21, 42, 63, 41, 75])
new_convert_arr = convert_arr.astype('f')
print('converted the array datatype to float ' + str(new_convert_arr))

#? Copying vs viewing 
'''
        The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

        The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

        The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''
#*Example of copying
copy_arr = np.array([22,33,44,55])
x = copy_arr.copy()
copy_arr[2] = 66
#! Note the output shows that the index 2 would be changed but printing out x would print out the original array
print('copied this array and changes a value ' + str(copy_arr)) 

#* Example of viewing 
view_arr = np.array([12, 14, 16, 18, 20])
y = view_arr.view()
view_arr[3] = 22
#! Note the output shows that the index 3 would be changed and the original array would also change
print('Viewing this array and changing a value ' + str(view_arr))


#* reshaping an array
# in the numpy_tuts1 we talked about shaping an array
reshap_arr = np.array([22,33,44,55,66,77,88,99,22,55])
new_reshap_arr = reshap_arr.reshape(5, 2) #* This creates 5 array with 2 values in each dimension
print('A reshaped array ' + str(new_reshap_arr))


#* reshaping 1-D to 3-D an array.... The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
reshap_arr_3d = np.array([22,33,44,55,66,77,88,99,00,00,99,88])
new_reshap_arr_3d = reshap_arr_3d.reshape(2,3,2)
print('A reshaped 3-dimensional array ' + str(new_reshap_arr_3d))