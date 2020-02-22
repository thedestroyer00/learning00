#creating a doubly linked list in python 
#Not a prefect one but it works fine...

class Node:
	def __init__(self, data = None):
		self.data = data 
		self.next = None
		self.prev = None


class Linkedlist:
	def __init__(self):
		self.head = None

	def push(self, newdata):
		NewNode = Node(newdata)
		NewNode.next = self.head
		if self.head is not None:
			self.head.prev = NewNode
		self.head = NewNode

	def insertitem(self, prev_node, newdata):
		if prev_node is None:
			return 
		NewNode = Node(newdata)
		NewNode.next = prev_node.next
		prev_node.next = NewNode
		NewNode.prev = prev_node
		if NewNode.next is not None:
			NewNode.next.prev = NewNode
	def appenditem(self,newdata):
		NewNode = Node(newdata)
		if self.head is None:
			NewNode.prev = None
			self.head = NewNode
			self.head.next = None
			return 
		last = self.head
		self.head = NewNode
		self.head.next = last
		last.prev = self.head


	def printlist(self,node):
		while node is not None:
			print(node.data)
			node = node.next

l = Linkedlist()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.printlist(l.head)
l.appenditem(5)
print("after appending an item in the list \n")
l.printlist(l.head)




