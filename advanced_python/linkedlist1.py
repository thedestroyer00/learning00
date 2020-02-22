class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None


class LinkeList:
	def __init__(self):
		self.head = None

	def push(self,newdata):
		NewNode = Node(newdata)
		if self.head is None:
			self.head = NewNode
			self.head.next = None
			return 

		else:
			last = self.head 
			while last is not None:
				prev = last
				last = last.next
			prev.next = NewNode
			
	def printlist(self):
		printvalue = self.head
		while printvalue is not None:
			print(printvalue.data)
			printvalue = printvalue.next


l = LinkeList()
l.push(1)
l.push(2)
l.push(3)
l.printlist()
