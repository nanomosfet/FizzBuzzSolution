class Node():
	def __init__(self, key, value):
		self.next = None
		self.value = value
		self.key = key

	def addNode(self, key, value):
		newNode = Node(key, value)
		n = self
		while n.next != None:
			n = n.next
		n.next = newNode

	def getNode(self, index):
		n = self
		for i in range(0,index):
			n = n.next
		return n

	def getValue(self, key):
		n = self
		while n.next != None:
			if n.key == key:
				return n.value
			n = n.next
		if n.key == key:
			return n.value
		return None
	def remove(self, key):
		# if self.key == key and self.next:
		# 	self.key = self.next.key
		# 	self.value = self.next.value
		# 	self.next = self.next.next
		# 	return True
		# elif self.next and self.next.key == key:
		# 	self.next = self.next.next
		# 	return True
		# elif not self.next and self.key != key:
		# 	return False
		# elif not self.next and self.key != key:
		# 	return False
		# else:
		# 	self.next.remove(key)

		if self.key == key:
			if self.next:
				print('self is %s, self.next is %s'%(self,self.next))
				self.key = self.next.key
				self.value = self.next.value				
				self.next = self.next.next
				return True
			else:
				return None				
		n = self
		while n.next != None:
			if n.next.key == key:
				n.next = n.next.next
				return True
			n = n.next
		return False

# node = Node('a', 1)
# node.addNode('b', 2)
# node.addNode('c', 3)
# node.addNode('d', 5)
# node.addNode('e', 6)
# node.remove('b')
# node.remove('e')
# print(node.getValue('b') == None)
# print(node.getValue('d') == 5)
# print(node.getValue('a') == 1)
# print(node.getValue('c') == 3)
# print(node.getValue('e') == None)

class HashTable():
	def __init__(self):
		self.linkedLists = [None,None,None,None,None,None]

	def hashFunction(self,key):
		return hash(key)%len(self.linkedLists)

	def addKeyPair(self, key, value):
		index = self.hashFunction(key)
		if self.linkedLists[index] == None:
			self.linkedLists[index] = Node(key, value)
		else:
			self.linkedLists[index].addNode(key, value)

	def getValue(self, key):
		index = self.hashFunction(key)

		if self.linkedLists[index] == None:
			return None
		else:
			return self.linkedLists[index].getValue(key)
	def removeValue(self, key):
		index = self.hashFunction(key)
		if self.linkedLists[index] == None:
			return False
		
		removeStatus = self.linkedLists[index].remove(key)
		if removeStatus == None:
			self.linkedLists[index] = None
			return True
		elif removeStatus == False:
			return False
		else:
			return True




hashtable = HashTable()

hashtable.addKeyPair('hello', 'from the other side')
hashtable.addKeyPair('test', '1234')
hashtable.addKeyPair('abcd', 'sdfdf')
hashtable.addKeyPair('ready', 'dfdfdf')
hashtable.addKeyPair('ready1234', '')
hashtable.addKeyPair('ready123', '')
print(hashtable.removeValue('abcd') == True)
print(hashtable.removeValue('not there') == False)
print(hashtable.removeValue('not theredfdf') == False)
print(hashtable.removeValue('not ') == False)


print(hashtable.getValue('hello') == 'from the other side')
print(hashtable.getValue('not') == None)
print(hashtable.getValue('ready1234') == '')
print(hashtable.getValue('abcd') == None)
print(hashtable.getValue('test') == '1234')
print(hashtable.getValue('not there') == None)


# testArray = [1,2,3,4,5,6,7]
# node = Node('hello',1)
# node.addNode('1234', 3)
# node.addNode('asdf', 123123123)
# print(node.getValue('hello') == 1)
# print(node.getValue('1234') == 3)
# print(node.getValue('123asdfasdfa4') == None)
def binarySearch(sortedArr, value):
	
	m = len(sortedArr)//2
	if m == 0:
		if sortedArr[m] == value:
			return True
		else:
			return False
	if sortedArr[m] > value:
		return binarySearch(sortedArr[:m], value)
	else:
		return binarySearch(sortedArr[m:], value)
arr = [1,7,5,9,2,12,3]

count = 0

# for i in range(0, len(arr)):
# 	for j in range(i+1, len(arr)):
# 		if abs(arr[j] - arr[i]) == 2:
# 			print('%d %d' %(arr[j], arr[i]))

# sortedArr = sorted(arr)

# # for i in sortedArr[:(len(sortedArr))//2]:
# # 	if binarySearch(sortedArr,i + 2):
# # 		print("%d %d"% (i, i+2)) 
# # 	if binarySearch(sortedArr,i - 2):
# # 		print("%d %d"% (i, i-2)) 
# hashtable = {}
# for i in range(0, len(arr)):
# 	hashtable[str(i)] = arr[i]

# for i in arr:
# 	if (i + 2) in hashtable.values() or (i - 2) in hashtable.values():
# 		print("%d %d"%(i, i + 2))




# print(binarySearch(sortedArr, 12))



