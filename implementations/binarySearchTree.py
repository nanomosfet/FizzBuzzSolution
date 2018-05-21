class Node():
	def __init__(self, value, parent=None):
		self.rightNode = None
		self.leftNode = None
		self.value = value
		self.parent = parent
		self.visited = False

	@property
	def depth(self):
		d = 0

		n = self
		while(n.parent):
			d += 1
			n = n.parent

		return d
	


	def isLeaf(self):
		return not (self.leftNode or self.rightNode)


	def hasRight(self):
		return self.rightNode != None
	
	def hasLeft(self):
		return self.leftNode != None

	def isRoot(self):
		return self.parent == None
	
	def isLeftNode(self):
		return (not self.isRoot()) and self.parent.leftNode == self

	def isRightNode(self):
		return (not self.isRoot()) and self.parent.rightNode == self



	def add(self, value):
		if value >= self.value:
			if self.rightNode == None:
				self.rightNode = Node(value, parent=self)
			else:
				self.rightNode.add(value)
		else:
			if self.leftNode == None:
				self.leftNode = Node(value, parent=self)
			else:
				self.leftNode.add(value)
	def search(self, value):
		if self.value == value:
			return self
		

		if value >= self.value:
			if self.rightNode == None:
				return False
			return self.rightNode.search(value)
		else:
			if self.leftNode == None:
				return False
			return self.leftNode.search(value)

	def findMinOfTree(self):
		if self.isLeaf():
			return self
		elif self.hasLeft():
			self.leftNode.findMinOfTree()
		else:
			return self


	def delete(self, value):
		if value == self.value:
			if self.isLeaf():
				if self.isRightNode():
					self.parent.rightNode = None
				else:
					self.parent.leftNode = None
			elif self.leftNode != None and self.rightNode == None:
				self.parent.leftNode = self.leftNode
				self.leftNode.parent = self.parent
				print('left node delete')
			elif self.rightNode != None and self.leftNode == None:
				self.parent.rightNode = self.rightNode
				self.rightNode.parent = self.parent
				print('right node delete')
			else:
				succ = self.rightNode.findMinOfTree()
				if self.isRightNode():
					self.parent.rightNode = succ
				elif self.isLeftNode():
					self.parent.leftNode = succ
				print(succ.value)
				self.value = succ.value
				self.rightNode.delete(succ.value)

				
		elif value >= self.value:
			if self.hasRight():
				self.rightNode.delete(value)
			else:
				return False
		else:
			if self.hasLeft():
				self.leftNode.delete(value)
			else:
				return False
	#def getLinkedListTree()








		







def traverseInOrder(node):
	if node != None:
		traverseInOrder(node.leftNode)
		print(node.value)
		traverseInOrder(node.rightNode)

def traversePreOrder(node):
	if node != None:
		print(node.value)
		traversePreOrder(node.leftNode)		
		traversePreOrder(node.rightNode)

def DepthLists(root):
	res = {}
	def search(node):
		if node != None:
			if node.depth in res:
				res[node.depth] = res[node.depth]+[node.value]
			else:
				res[node.depth] = [node.value]
			search(node.rightNode)
			search(node.leftNode)
	search(root)
	return res

myNode = Node(5)
myNode.add(4)
myNode.add(3)
myNode.add(2)
myNode.add(6)
myNode.add(7)
myNode.add(3)
myNode.add(2)
# myNode.delete(5)
# myNode.delete(2)
# myNode.delete(3)
# myNode.delete(3)

print(myNode.search(2))
print(myNode.search(4))
print(myNode.search(7))
print(myNode.search(200))
print(myNode.search(1))
print(myNode.search(5))
#traverseInOrder(myNode)

print(DepthLists(myNode))




