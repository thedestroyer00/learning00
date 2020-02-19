# Trying to create a linked list but this code doesn't works

class Node:
	def __init__(self, data= None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head =None

	def push(self, newdata):
		value = self.head
		NewNode = Node(newdata)
		if value is None:
			self.head = NewNode
		else:
			while value is not None:
				value = value.next
			value = NewNode

	def printlist(self):
		printvalue = self.head
		while printvalue is not None:
			print(printvalue.data)
			printvalue = printvalue.next


l = LinkedList()
l.push(5)
l.push(6)
l.push(7)
l.printlist()
