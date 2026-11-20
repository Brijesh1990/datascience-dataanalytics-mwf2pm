# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(arr.dtype)
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])

# additions of indexing 
# print(arr[0] + arr[3])
# print(arr[0] - arr[3])
# print(arr[0] / arr[3])
# print(arr[0] * arr[3])
# print(arr[0] % arr[3])

# print(arr.__index__)

import numpy as np
arr=np.array([1,2,3,4,5])
# print(arr[0])
# index = np.where(arr == 3)
# print(index[0]) # give index where 3 is stored in array

# index = np.where(arr == 1)
# print(index[0]) # give index where 3 is stored in array


index = np.where(arr == 5)
print(index[0]) # give index where 3 is stored in array