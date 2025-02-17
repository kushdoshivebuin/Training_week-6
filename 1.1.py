import numpy as np 

x = np.array([5, 2, 3])

y = np.array([[1, 2], [3, 4]])

z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Performing shape, dtype, ndim, +, dot
print("1D array : \n", x)
print("Shape of the array : ", x.shape) # Shape denotes the shape of the array : here it will (3,)
print("Data type of the array : ", x.dtype)  # dtype prints the datatype of the array : int64
print("Dimension of the array : ", x.ndim)   # Dimension of the array : 1 
print("\n2D array : \n", y)
print("Shape of the array : ", y.shape)  # Here it will print (2, 2)
print("Data type of the array : ", y.dtype)  # Data type of the array
print(y.ndim)   # Dimension of the array : 2
print("\n3D array : \n", z)
print("Shape of the array : ", z.shape)  # Here it will print (2, 2, 2)
print("Data type of the array : ", z.dtype)  # Data type of the array
print("Dimension of the array : ", z.ndim)   # Dimension of the array : 3

# print("Addition of the x and y : ", x + y) # Not possible as it needs same dimensions for operation

y = np.array([4, 5, 6])
print("\nAddition of x and y : ", x + y)
print("\nDot product of x and y : ", np.dot(x, y))

# Performing zeros
zeroarray = np.zeros((2, 3))
print("\nAn array filled with zeros of dimension 2 and shape (2, 3)", zeroarray)
print(zeroarray.ndim, zeroarray.shape)

# Performing ones
onearray = np.ones((2, 3))
print("\nAn array filled with ones of dimension 2 and shape (2, 3)", onearray)
print(onearray.ndim, onearray.shape)

# np.arange function
arangearray = np.arange(1, 11, 2)
print("\nThis will generate an array in the given range start : 1, stop : 11, step : 2\n", arangearray)

# np.linspace function
linear_array, step = np.linspace(0, 1, 5, retstep=True)
print("\nThis will generate 5 elements between the given range at equal intervals\n", linear_array, " and the step size is : ", step)

# np.random function
randomarray = np.random.rand(2, 3)
print("\nThis will generate a random array between 0 and 1 of the shape(2, 3)\n", randomarray)

randomarray = np.random.randint(1,10)
print("\nThis will generate a random integer between the given range : ", randomarray)

# np.reshape function
reshaped = np.reshape(np.arange(6), (2, 3))
print("\nThis will generate integers from 0 to 5 and reshape into shape(2, 3) :\n", reshaped)

# flatten function
flatten = reshaped.flatten()
print("\nThis will flatten the reshaped array into one dimension :\n", flatten)

# Transpose function
transpose = reshaped.T
print("\nThis will transpose the matrix :\n", transpose)

# concatenate function
concatenated = np.concatenate((x, y))
print("\nThis will concatenate the two arrays : x and y:\n", concatenated)

# sum function
total = np.sum(x)
print("\nThis will add the elements present in the array : \n", total)

# mean function
mean_value = np.mean(x)
print("\nThis will print the mean of the values of the array :\n", mean_value)

# max and min function
max_value = np.max(x)
min_value = np.min(x)
print("\nThe max value is :",max_value," and the min value is :",min_value)

# sqrt function
sqrt_value = np.sqrt(x)
print("\nThis will print the square root of all the elements in the array :", sqrt_value)

# Indexing and slicing
second_element = x[1]
print("\nThis is the second element of the array :",second_element)

slicing = x[1:3]
print("\nThis will print the array's 2nd and 3rd element : ",slicing)

# Sorting
sorted_array = np.sort(x)
print("This will sort the array in ascending order by default :", sorted_array)

# Indices
indices = np.argsort(x)
print("This will return the indices of the sorted elements : ", indices)

# np.where
condition = np.where(x>2)
print("Array indice where the elements are greater than 2 :", condition)

# Convert a 2D array into 4D
y = np.array([(1, 2), (3, 4)]) 
dim = np.reshape(y, (1, 1, 2, 2))
print(dim)

# np.take function
array = [[5, 6, 2, 7, 1], 
		[4, 9, 2, 9, 3]] 
print("\nOriginal array : \n", array) 

print("\nTaking Indices\n", np.take(array, [0, 3])) 

print("\nTaking Indices axis = 0\n", np.take(array, [0, 1], axis = 0))
print("\nTaking Indices axis = 1\n", np.take(array, [0, 4], axis = 1))

# np.extract
array = np.arange(10).reshape(5, 2) 
print("Original array : \n", array) 
  
a = np.mod(array, 4) !=0
# This will show element status of satisfying condition 
print("\nArray Condition a : \n", a) 
  
# This will return elements that satisfy condition "a" condition 
print("\nElements that satisfy condition a  : \n", np.extract(a, array)) 

b = array - 4 == 1
# This will show element status of satisfying condition 
print("\nArray Condition b : \n", b) 

# This will return elements that satisfy condition "b" condition 
print("\nElements that satisfy condition b  : \n", np.extract(b, array))