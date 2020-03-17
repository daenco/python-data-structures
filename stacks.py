# Implementation using list

# # Python program to demostrate stack implementation
# # using list

# stack = []

# # append() function to push element in the stack
# stack.append("a")
# stack.append("b")
# stack.append("c")

# print("Initial stack")
# print(stack)

# # pop() function to pop element from stack in LIFO order
# print("\nElements popped from stack:")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print("\nStack after elements are popped:")
# print(stack)

# # Output:
# Initial stack
# ['a', 'b', 'c']

# Elements popped from stack:
# c
# b
# a

# Stack after elements are popped:
# []



# # Implementation using collections.deque

# from collections import deque

# stack = deque()

# # append() function to push element in the stack
# stack.append("a")
# stack.append("b")
# stack.append("c")

# print("Initial stack:")
# print(stack)

# # pop() function to pop element from stack in
# # LIFO order
# print("\nElements popped from stack:")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print("\nStack after elements are popped:")
# print(stack)

# Output: 
# Initial stack:
# deque(['a', 'b', 'c'])

# Elements popped from stack:
# c
# b
# a

# Stack after elements are popped:
# deque([])



# # Implementation using queue module

# # Python program to demostrate stack implementation
# # using queue module

# from queue import LifoQueue

# # Initializing a stack
# stack = LifoQueue(maxsize=3)

# # qsize() show the number of elements in the stack
# print(stack.qsize())

# # put() function to push element in the stack
# stack.put("a")
# stack.put("b")
# stack.put("c")

# print("Full: ", stack.full())
# print("Size: ", stack.qsize())

# # get() function to pop element from stack in LIFO order
# print("\nElements popped from the stack")
# print(stack.get())
# print(stack.get())
# print(stack.get())

# print("\nEmpty: ", stack.empty())

# Ouput:

# 0
# Full:  True
# Size:  3

# Elements popped from the stack
# c
# b
# a

# Empty:  True