
#* numpy dot product or matrix multiplication
import numpy as np
#* Example
arr_one = np.array([[1,2], [3,4]])
arr_two = np.array([[33,44], [45,46]])
#! How the dot product is computed >> [ 1*33+2*45 , 1*44+2*46 ],[ 3*33+4*45 , 3*44+4*46 ]
matrix = np.dot(arr_one, arr_two)
print('Matrix multiplication ' + str(matrix))


#* Using the @ to create the dot product
at_sign = arr_one @ arr_two
print('Using the @ symbol to create the dot product ' + str(at_sign))
#This method is easier and you'd see this in many code. 

#* Numpy concatination 
#*example
arr_conc_one = np.array([[22,23], [24,25]])
arr_conc_two = np.array([[26,27], [28,29]])
concatenate = np.concatenate((arr_conc_one, arr_conc_two))
print('Concatinated arrays ' + str(concatenate))