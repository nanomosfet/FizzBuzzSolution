import string

def isUniqueChars(s):
	table = {}
	for c in string.ascii_lowercase:
		table[c] = 0
	
	index = 0
	for c in s:
		table[c] += 1
		if table[c] > 1: 
			return False
	return True


print(isUniqueChars('abcdefghijklmnop') == True)
print(isUniqueChars('asdfasdfasdfasdfasdfasdf') == False)

def isPermutationOfOther(str1, str2):
	if sorted(str1) == sorted(str2) :
		return True
	else:
		return False

print(isPermutationOfOther('aaaaaaa','aaaaaaa') == True)
print(isPermutationOfOther('asdfas','safdsa') == True)
print(isPermutationOfOther('abccba','abccba') == True)
print(isPermutationOfOther('aaaaaaa','aaaa') == False)
print(isPermutationOfOther('aaaaaaa','aaasdfasdfaa') == False)
print(isPermutationOfOther('aaaaaasdfasdfasdfasdfsadfasdfaa','aaasdfasdfaa') == False)

def permIsPalan(s):
	charCount = {}
	for c in string.ascii_lowercase:
		charCount[c] = 0

	stripedS = s.replace(' ', '')
	countEven = 0
	countOdd = 0

	for c in stripedS:
		charCount[c] += 1

	for key in charCount:
		if charCount[key]%2 == 0:
			countEven += 1
		else:
			countOdd += 1
	if countOdd <= 1:
		return True
	else:
		return False

print(permIsPalan('taco coa') == True)
print(permIsPalan('racecar') == True)
print(permIsPalan('race   car') == True)
print(permIsPalan('racecarr') == False)
print(permIsPalan('abcdefgfedcba') == True)
print(permIsPalan('aaaaaaaaaaaaaaaaaaa') == True)
print(permIsPalan('aaaaaaaaaaaaaaaaaaaa') == True)


def createMinTree(sortedArr, minTree = []):
	if not len(sortedArr):
		return
	elif len(sortedArr) <= 2:
		for el in sortedArr:
			minTree.append(el)
	else:
		midIdx = (len(sortedArr) - 1) // 2
		minTree.append(sortedArr[midIdx])
		createMinTree(sortedArr[midIdx+1:], minTree)
		createMinTree(sortedArr[:midIdx], minTree)
	return minTree


assert createMinTree([1,2,3,4,5,6,7,8],minTree = []) == [4, 6, 7, 8, 5, 2, 3, 1]
assert createMinTree([50,100,101,200,300,1000,1001,1004,1006], minTree = []) == [300, 1001, 1004, 1006, 1000, 100, 101, 200, 50]



def kthSmallestEl(arr):
	smallestArrayPossible
	for el in arr:
		if 

