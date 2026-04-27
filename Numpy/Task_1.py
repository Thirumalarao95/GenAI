import numpy as np
# Create a 1D array of integers from 0 to 9
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10])
print("1D Array:", array_1d)
array_2d = np.arange(1,10)
my_list = [10, 20, 30, 40, 50]


my_array = np.array(my_list)
array_2d = array_2d.reshape(3,3)
print("2D Array:\n", array_2d)
print(np.shape(array_2d))
print(np.shape(array_1d))
print(np.shape(my_array))
print(type(array_1d))
print(type(array_2d))
print(type(my_array))
