# # Implementation using list

# # Python program to demonstrate queue implementation
# # using list

# # Initializing a queue
# queue = []

# # Adding elements to the queue
# queue.append("a")
# queue.append("b")
# queue.append("c")

# print("Initial queue")
# print(queue)

# # Removing elements from the queue
# print("Elements dequeued from queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

# print("\nQueue after removing elements")
# print(queue)

# # Output:

# # Initial queue
# # ['a', 'b', 'c']
# # Elements dequeued fro queue
# # a
# # b
# # c

# # Queue after removing elements
# # []



# # Implementation using collections.deque

# # Python program to demonstrate queue implementation
# # using collections.dequeue

# from collections import deque

# # Initializing a queue
# q = deque()

# # Adding elements to a queue
# q.append("a")
# q.append("b")
# q.append("b")

# print("Initial queue")
# print(q)

# # Removing elements from a queue
# print("\nElements dequeued from the queue")
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# print("\nQueue after removing elements")
# print(q)

# # Output:

# # Initial queue
# # deque(['a', 'b', 'b'])

# # Elements dequeued from the queue
# # a
# # b
# # b

# # Queue after removing elements
# # deque([])



# # Implementation using queue.Queue

# # Python program to demonstrate implementation of
# # queue using queue module

# from queue import Queue

# # Initialing a queue
# q = Queue(maxsize=3)

# # qsize() give the maxsize of the Queue
# print(q.qsize())

# # Adding of element to queue
# q.put("a")
# q.put("b")
# q.put("c")

# # Return Boolean for full Queue
# print("\nFull: ", q.full())

# # Removing element from queue
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())

# # Return Boolean for Empty Queue
# print("\nEmpty: ", q.empty())

# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())

# # Output:

# # 0

# # Full:  True

# # Elements dequeued from the queue
# # a
# # b
# # c

# # Empty:  True

# # Empty:  False
# # Full:  False
