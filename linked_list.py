# # A simple python program for traversal of a linked list

# # Node class
# class Node:

# 	# Function to initialize the node object
# 	def __init__(self, data):
# 		self.data = data # Assign data
# 		self.next = None # Initialize next as null

# # Linked List class contains a Node object
# class LinkedList:

# 	# Function to initialize head
# 	def __init__(self):
# 		self.head = None

# 	# This function prints contents of linked list
# 	# starting from head
# 	def printList(self):
# 		temp = self.head
# 		while temp:
# 			print(temp.data)
# 			temp = temp.next

# # Code execution starts here
# if __name__ == "__main__":

# 	# Start with the empty list
# 	llist = LinkedList()

# 	llist.head = Node(1)
# 	second = Node(2)
# 	third = Node(3)

# 	llist.head.next = second # Link first node with second
# 	second.next = third # Link second node with the third node

# 	llist.printList()

# 	# Ouput:
# 	# 1
# 	# 2
# 	# 3



class Node:

	def __init__(self, data=None):
		self.data = data
		self.next =None

class SLinkedList:

	def __init__(self):
		self.head = None

list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.head.next = e2
e2.next = e3