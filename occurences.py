"""
	Filename: occurences.py
	Author: David Docteur
	Date: 22/08/2017
	Description: This script detects strings contained in other lists,
	  including the number of unique and total strings as well.
	  The logic used here is based on a circular singly linked list
	  for which each node has a pointer to the next one, the last one points
	  back to the first(head) of the list.
	Version: Python v3.6.0
"""


class Node:
	"""
		This class represents a node in the singly linked list.
		Each node has a pointer to the next one and some data,
		which is the list of strings that has been defined by the user.
	"""

	data = None

	def __init__(self, data):
		"""
			Constructor - initialises a node.
		"""
		self.data = data
		self.next = None
		
	def getData(self):
		"""
			Returns the list of strings contained in the node.
		"""
		return self.data

	def getNext(self):
		"""
			Returns the next node pointer by the current one.
		"""
		return self.next
		
	def setNext(self, node):
		"""
			Sets the next node pointed by the current one.
		"""
		self.next = node

		
class LinkedList:
	"""
		This class represents the circular singly linked list.
		This one is single - nodes only have pointers to the next one.
		The usage of a doubly linked list here could have worked but
		unecessary and would have required more memory, which could
		be inconvenient when working on some limited amount of memory.
	"""

	head = None

	def __init__(self):
		self.head = None
		self.current = None
		
	def isEmpty(self):
		return self.head == None
		
	def getHead(self):
		return self.head
	
	def setHead(self, node):
		self.head = node;
		
	def setCurrent(self, node):
		self.current = node;
		
	def getCurrent(self):
		return self.current
	
	def setNext(self, node):
		self.next = node
	
	def addNode(self, data):
		"""
			Adds a node to the linked list - the head points to itself
			if it is the very first node to be inserted, otherwise
			add the next one, make the previous one point to it
			and this new node points then to the head to make it
			circular.
		"""
		if self.isEmpty(): 
			self.setHead(Node(data))
			self.setCurrent(self.getHead())
			# Circular linkedlist, if only the head, then points to itself
			self.getCurrent().setNext(self.getCurrent())
		else:
			temp = Node(data)
			self.getCurrent().setNext(temp)
			self.setCurrent(temp)
			# Circular linked list, the last element points back to the head
			self.getCurrent().setNext(self.getHead())

	def countNodes(self):
		"""
			As the list is circular, count by going to the next element
			until the head is reached again.
		"""
		count = 1
		currentNode = self.getHead()
		
		# What if no nodes have been created?
		if self.getHead() == None:
			return 0
		
		while currentNode.getNext() != self.getHead():
			count += 1
			currentNode = currentNode.getNext()
			
		return count
			
			
def process_lists(llist):
	"""
		Function that takes a list of lists as a parameter and
		calculates the amount of duplicates, unique and total strings.
		This function starts from the first node of the list, goes through each
		string and check if it exists in other nodes. Then it processes the next ones.
		Even if the current node is in the middle of the list, the circular list allows
		the algorithm to go through each node until it comes back to it and stop.
		If a string has already been found as a duplicate, then the algorithm
		won't even try to look for it, for better performance.
	"""
	
	currentNode = head = llist.getHead()
	occurences = {}
	# Not in the requirement, but it could tell us how many times
	# a string has been found in other lists.
	dups = 0
	count = 0
	uniques = 0
	total = 0
	
	# Go through each node
	while count < llist.countNodes():
		# Loop throught each string in the current list
		for sequence in currentNode.getData():
			total += 1
			# If string has been processed already, no need to do it again
			if sequence in occurences:
				continue
			nextNode = currentNode.getNext()
			while nextNode is not currentNode:
				# Count duplicates
				if sequence in nextNode.getData():
					dups += 1
					occurences[sequence] = dups
					
				nextNode = nextNode.getNext()
			if sequence not in occurences:
				uniques += 1
		# Let's process the strings from the next node
		currentNode = currentNode.getNext()
		dups = 0
		count += 1
		
	occurences_found = ''
	for key in occurences:
		occurences_found += str(key) + " "
	
	print("Strings appearing in multiple lists: " + occurences_found)
	print("Number of unique strings: " + str(uniques))
	print("Total number of strings processed: " + str(total))
	#end while
	
	return occurences_found, uniques, total

	
def input_list():
	"""
		This function takes a comma separated list of characters
		from the user input and returns it as a list.
	"""
	
	# User input
	stdin = ''
	# Current number of lists
	num_list = 0
	linkedl = LinkedList()
	
	print("Please, type a comma separated list. Press enter for the next list,\
	type 'exit' to finish input.\n")
	while stdin != 'exit':
	
		num_list += 1
		
		# Be careful here, spaces can be accepted as part of a string here
		# but again, it depends on the requirement. Spaces could be stripped
		# or replaced with replace(" ", "").
		stdin = input("List #" + str(num_list) + "\n")
				
		if stdin == 'exit':
			return linkedl
	
		if stdin != "":
			# Split user input into a list
			chars_list = stdin.split(',')
			linkedl.addNode(chars_list)
		else:
			num_list -= 1
			print("You must type at least one character.")
		
	# end while

		
if __name__ == "__main__":
	llist = input_list()
	(occurences, uniques, total) = process_lists(llist)
