class MinHeap(object):
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0
	

	def insert(self, value):
		self.heapList.append(value)
		self.currentSize += 1
		self.bubbleUp(self.currentSize)

	def remove(self, value):
		pass
	
	def extractMin(self):
		pass
	
	def reset(self):
		self.heapList = [0]
		self.currentSize = 0

	def bubbleUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2



heap = MinHeap()

assert heap.heapList == [0]

arr = range(0,10)
for el in arr:
	heap.insert(el)
try:
	assert heap.heapList == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
except AssertionError:
	print(heap.heapList)
heap.reset()
arr = [4,3,2,1]
for el in arr:
	heap.insert(el)

try:
	assert heap.heapList == [0, 1, 2, 3, 4]
except:
	print(heap.heapList)