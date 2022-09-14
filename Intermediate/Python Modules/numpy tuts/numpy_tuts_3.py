
import numpy as np
#* Empty array
empty_array = np.zeros((2,2))
print('Empty array ' + str(empty_array))

#* ones 
ones_array = np.ones((2,2))
print('Ones array ' + str(ones_array))

#* eye array
eye_array = np.eye(6)
print('Eye array ' + str(eye_array))

#* eye array but changing values 
eye_array_two = np.eye(5)
eye_array_two[eye_array_two == 0] =2
print('Eye array but replaced value(1) to (2) ' + str(eye_array_two))

# other filtering functions 
eye_array_two = np.eye(5)
eye_array_two[eye_array_two < 2] = 4
print('Eye array but replaced value(1) to (2) ' + str(eye_array_two))

