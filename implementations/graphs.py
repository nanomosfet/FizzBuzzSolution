class Queue():
	def __init__(self):
		self.first = None
		self.last = None

	class QueueNode():
		def __init__(self, data):
			self.data = data
			self.next = None

	def isEmpty(self):
		return self.first == None
	
	def add(self, item):
		t = self.QueueNode(item)
		if self.last != None:
			self.last.next = t
		self.last = t
		if self.first == None:
			self.first = self.last

	def remove(self):
		if self.first == None:
			raise Exception('No Such Element')

		data = self.first.data
		self.first = self.first.next
		if self.first == None:
			self.last = None
		return data


class Graph():
	def __init__(self):
		self.nodes = []




class DirectedGraph(Graph):
	def __init__(self):
		Graph.__init__(self)


	def addNode(self, node):
		self.nodes.append(node)

	def addEdge(self, nodeSrc, nodeDest):
		if nodeSrc in self.nodes and nodeDest in self.nodes:
			if nodeDest not in nodeSrc.children:
				nodeSrc.addChild(nodeDest)
			else:
				raise Exception('Edge Exists already')
		else:
			raise Exception('Node not found in graph')
	def neighbors(self, node):
		if node in self.nodes:
			return [neighbor for neighbor in node.children]
		else:
			raise Exception('Node not found in graph')

	def removeEdge(self, nodeSrc, nodeDest):
		if nodeSrc in self.nodes and nodeDest in self.nodes:
			if nodeDest in nodeSrc.children:
				nodeSrc.children.remove(nodeDest)
		else:
			raise Exception('Edge not found in graph')
	
	def getNodeValue(self, node):
		return node.value

	def unmarkAllNodes(self):
		for node in self.nodes:
			node.marked = False

	def getRoot(self):
		return self.nodes[0]

	def getNodeByValue(self, value):
		return next(filter(lambda a: a.value == value, self.nodes))

	def depthFirstSearch(self, root):
		if root == None:
			return
		self.visit(root)
		root.marked = True
		for n in root.children:
			if n.marked == False:
				self.depthFirstSearch(n)


	def visit(self, node):
		pass
		# print("I have visited Node: %s" % node.value)

	def breadthFirstSearch(self, root):
		queue = Queue()
		queue.add(root)
		root.marked = True		
		while(not queue.isEmpty()):
			node = queue.remove()
			self.visit(node)
			
			for child in node.children:
				if not child.marked:
					queue.add(child)
					child.marked = True
	def routeExists(self, a, b):
		def displayRoute(valueSrc, valueDest, routeLog):
			print(routeLog[valueSrc+'-'+valueDest])


		if a == b:
			return True
			
		queue = Queue()
		queue.add(a)
		a.marked = True
		routeLog = {}
		while not queue.isEmpty():
			currentNode = queue.remove()
			self.visit(currentNode)		
			for child in currentNode.children:
				if not child.marked:
					if currentNode == a:
						routeLog[a.value+'-'+child.value] = [currentNode.value,child.value]
					else:
						routeLog[a.value+'-'+child.value] = routeLog[a.value+'-'+currentNode.value]+[child.value] # 1 for away
					
					if child == b:
						displayRoute(a.value, b.value, routeLog)
						return True
					queue.add(child)
					child.marked = True
		return False






class Node():
	def __init__(self, value):
		self.value = value
		self.marked = False
		self.children = []

	def addChild(self, node):
		self.children.append(node)



# tests
q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)

assert q.remove() == 1
assert q.remove() == 2
assert q.remove() == 3
assert q.isEmpty() == False
assert q.remove() == 4
assert q.isEmpty() == True

def printAdjacencyList(graph):
	for node in graph.nodes:
		print({node.value: [node.value for node in graph.neighbors(node)]})

# node1 = Node('Tim')
# node2 = Node('Jessica')
# node4 = Node('Travis')

names = ['tim', 'travis', 'jessica', 'juan', 'teddy', 'dan', 'jerry', 'fits', 'leny']
graph = DirectedGraph()
# for name in names:
# 	graph.addNode(Node(name))

g2 = {
	'tim': ['jessica', 'travis', 'teddy', 'leny'],
	'jessica': ['tim', 'travis'],
	'john': ['teddy', 'jerry'],
	'travis': ['dan', 'teddy', 'john'],
	'larry': ['dan', 'teddy', 'john'],
	'phil': ['teddy', 'david'],
	'jerry': ['dan', 'phil'],
	'dan': ['teddy', 'john'],
	'david': ['jessica', 'teddy', 'john'],
	'teddy': ['jessica', 'leny', 'john'],
	'leny': ['jessica', 'teddy', 'john', 'larry'],
	'greg': ['jessica', 'teddy', 'john', 'larry'],
}

g = {'A': ['B', 'C'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C'],
     'E': ['F'],
     'F': ['C']}

for key in g:
	graph.addNode(Node(key))
	
for key in g:
	for person in g[key]:
		graph.addEdge(graph.getNodeByValue(key), graph.getNodeByValue(person))

#graph.depthFirstSearch(graph.getRoot())
# graph.breadthFirstSearch(graph.getRoot())

assert graph.routeExists(graph.getNodeByValue('A'), graph.getNodeByValue('D')) == True
graph.unmarkAllNodes()
assert graph.routeExists(graph.getNodeByValue('A'), graph.getNodeByValue('F')) == False

# for name in names:

# 	choice1 = graph.getNodeByValue(random.choice(names))
# 	name = graph.getNodeByValue(name)
# 	if 
# 	graph.addEdge()



# assert graph.getNodeByValue('tim').value == 'tim'

# graph = DirectedGraph()
# graph.addNode(node1)
# graph.addNode(node2)
# graph.addNode(node3)
# graph.addEdge(node1, node2)
# graph.addEdge(node1, node3)
# graph.addEdge(node2, node3)

# graph.depthFirstSearch(graph.getRoot())
#printAdjacencyList(graph)

#printAdjacencyList(graph)

