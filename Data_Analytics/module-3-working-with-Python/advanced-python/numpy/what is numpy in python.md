# what is numpy in python ? 
1. numpy is used for computing in python
2. numpy is an third party library of python
3. numpy is used for working with array in python 
4. numpy is used for working with matrices in python 
5. numpy is used for linear algebra  in python 
6. numpy is used for random numbers in python 
7. numpy is also used for statistics in python 
   **exmaples**
   1. mean 
   2. average 
   3. max
   4. median 
   5. mode 
8.  numpy is also used for AI 
9.  numpy is also used in da & ds 
10. numpy is also used for big data 
11. numpy is also used for data manipulations
12. numpy is also used for data cleaning in python 
13. numpy is also used for data processing 


# how to install numpy

1. python -m pip install numpy 
2. python pip show numpy 
3. import numpy as np
4. details of numpy

```
Name: numpy
Version: 2.5.1
Summary: Fundamental package for array computing in Python
Home-page: https://numpy.org
Author: Travis E. Oliphant et al.
Author-email:
License-Expression: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
Location: C:\Users\Admin\AppData\Roaming\Python\Python314\site-packages
Requires:
Required-by: contourpy, matplotlib, pandas, pydeck, seaborn, streamlit, transformers
```

# advantages of using numpy ?

1. numpy is faster than python list
2. numpy is more efficient than python list
3. numpy is more flexible than python list 
4. numpy is more readable than python list 
5. numpy is more scalable than python list
6. numpy is more maintainable than python list
7. numpy is more versatile than python list 

  **examples of array**

  ```
  import numpy as np
  arr=np.array(["om","faiz","meet","rushikesh","forum","mishri"])
  print(arr)
  print(type(arr))
  ```

# types of array defined in python using numpy ?

1. 0-dimensional array(scalar)
2. 1-dimensional array(vector)
3. 2-dimensional array(matrix)
4. n-dimensional array(tensor)

# 0-dimensional array(scalar)

1. A scalar is a single value that can be represented as 0-dimensional array in numpy
2. It is the simplest form of an array and does not have any dimension

**examples**

```
# 0-dimensional array
import numpy as np 
arr=np.array(10)
print(arr)

```


# 1-dimensional array(vector)

1. A vector  is a one-dimensional array that can be represented 1-dimensional  array in numpy
2. It is the sequence of values that can be indexed and sliced just like a list [1,2,4,5,6]

**examples**

```
# 1-dimensional array
import numpy as np 
arr=np.array([1,2,3,4,5,6])
print(arr)

```


# 2-dimensional array(matrix)

1. A matrix  is a two-dimensional array that can be represented 2-dimensional  array in numpy or also called matrix in python 
2. It is a rectangular array of values that can be indexed and sliced just like list [[1,2],[3,4]]

**examples**

```
# 2-dimensional array
import numpy as np 
arr=np.array([[1,2],[3,4]])
print(arr)
print(arr[0])
print(arr[1])

```



# n-dimensional array(tensor)

1. A tensor  is a multi-dimensional array that can be represented n-dimensional  array in numpy or also called tensor in python

2. It is a generalized of scalars, vectors and matrices to higher dimensions of array to stored data [[[1,2],[3,4]],[[5,6],[7,8]]]


**examples**

```
# n-dimensional array or tensor
import numpy as np 
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr)
print(arr[0])
print(arr[1])

```