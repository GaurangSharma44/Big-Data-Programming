import numpy as np

print("\nExercise 1")
array1 = np.arange(0,10)
print("Original: \n",array1)
print("After replacing all odd numbers with -1: \n",np.where(array1 % 2 == 1,-1,array1))

print("\nExercise 2")
array2 = np.arange(10)
print("Original: \n",array2)
print("After converting an 1D array to a 2D array: \n",np.reshape(array2,(2,5)))

print("\nExercise 3")
array3 = np.arange(1,4)
print("Original: \n",array3)
a3 = np.repeat(array3, 3)
b3 = np.tile(array3, 2)
print("After generating a custom sequence: \n",np.concatenate((a3,b3),axis=0))

print("\nExercise 4")
a4 = np.array([1,2,3,2,3,4,3,4,5,6])
b4 = np.array([7,2,10,2,7,4,9,4,9,8])
print("a4: \n",a4)
print("b4: \n",b4)
print("After getting common items between a & b: \n",np.intersect1d(a4,b4))

print("\nExercise 5")
a5 = np.array([1,2,3,2,3,4,3,4,5,6])
b5 = np.array([7,2,10,2,7,4,9,4,9,8])
print("a5: \n",a5)
print("b5: \n",b5)
print("After getting positions of common element: \n",np.nonzero(np.in1d(a5, b5))[0])

print("\nExercise 6")
print("Creating a 2D random array of shape 5,3 with random floats between 5 and 10: \n",np.random.uniform(5,10, size=(5, 3)))

print("\nExercise 7")
array7 = np.arange(15)
print("Original: \n",array7)
np.set_printoptions(threshold=6)
print("After limiting the numbers printed in an array: \n",array7)

print("\nExercise 8")
np.random.seed(100)
array8 = np.random.random([3,3])/1e3
print("Original: \n",array8)
np.set_printoptions(suppress=True)
print("After supressing: \n",array8)

print("\nExercise 9")
array9 = np.arange(9).reshape(3,3)
print("Original: \n",array9)
array9[:,[0, 1]] = array9[:,[1, 0]]
print("After swapping columns: \n",array9)

print("\nExercise 10")
array10 = np.arange(9).reshape(3,3)
print("Original: \n",array10)
array10[[0, 2],:] = array10[[2, 0],:]
print("After swapping rows: \n",array10)