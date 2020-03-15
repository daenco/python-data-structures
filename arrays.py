# # Python code to demonstrate the working of array(), append(), insert()

# # Importing array module for array operations
# import array

# # Initializing array with array values
# # Initializes array with signed integers
# arr = array.array("i", [1, 2, 3])

# # Printing original array
# print("The new created array is: ", end=" ")
# for i in range(0, 3):
# 	print(arr[i], end=" ")
# print()

# # Using append() to insert new value at end
# arr.append(4)

# # Printing appended array
# print("The appended array is: ", end=" ")
# for i in range(0, 4):
# 	print(arr[i], end=" ")
# print()

# # Using insert() to insert value at specific position
# # inserts 5 at 2nd position
# arr.insert(2, 5)

# # Printing array after insertion
# print("The array after insertion is: ", end=" ")
# for i in range(0, 5):
# 	print(arr[i], end=" ")
# print()

# # Output:
# # The new created array is:  1 2 3 
# # The appended array is:  1 2 3 4 
# # The array after insertion is:  1 2 5 3 4 



# # Python code to demonstrate the working of pop()
# # and remove()

# # Importing array for array operations
# import array

# # Initializing array with array values initializes
# # array with with signed integers
# arr = array.array("i", [1, 2, 3, 1, 5])

# # Printing original array
# print("The new created array is: ", end="")
# for i in range(0, 5):
# 	print(arr[i], end=" ")
# print()

# # Using pop() to remove element at 2nd position
# print("The popped element is: ", end="")
# print(arr.pop(2))

# # Printing array after popping
# print("The array after popping is: ", end="")
# for i in range(0, 4):
# 	print(arr[i], end=" ")
# print()

# # Using remove() to remove 1st occurrence of 1
# arr.remove(1)

# # Printing array after removing
# print("The array after removing is: ", end="")
# for i in range(0, 3):
# 	print(arr[i], end=" ")
# print()

# # Ouput:
# # The new created array is: 1 2 3 1 5 
# # The popped element is: 3
# # The array after popping is: 1 2 1 5 
# # The array after removing is: 2 1 5



# # Python code to demonstrate the working of index()
# # and reverse()

# # Importing array for array operations
# import array

# # Initializing array with array values
# # Initializes array with signed integers
# arr = array.array("i", [1, 2, 3, 1, 2, 5])

# # Printing original array
# print("The new created array is: ", end="")
# for i in range(0, 6):
# 	print(arr[i], end=" ")
# print()

# # Using index() to print index of 1st occurrence of 2
# print(arr.index(2))

# # Using reverse() to reverse the array
# arr.reverse()

# # Printing array after reversing
# print("The array after reversing is: ", end="")
# for i in range(0, 6):
# 	print(arr[i], end=" ")
# print()

# # Output:

# # The new created array is: 1 2 3 1 2 5 
# # 1
# # The array after reversing is: 5 2 1 3 2 1 
