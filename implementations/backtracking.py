# class Solution:
#     def readBinaryWatch(self, num):
#         """
#         :type num: int
#         :rtype: List[str]
#         """
#         if num == 0:
#             return ['0:00']
#         result = []
        
#         self._readBinaryWatch(num, result, out = [0]*10)
#         return sorted(result, key= lambda x: int(x.split(':')[0]*10*10+ x.split(':')[1]))
        
#     def _readBinaryWatch(self, num, result, pos = 0, out = [0]*10):
#         outCopy = list(out)
#         if num == 0:
#             resTime = self.binToTime(outCopy)
#             print(outCopy)
#             print(resTime)
#             if resTime == '0:00':
#                 pass
#             else:
#                 result.append(self.binToTime(outCopy))
#                 return
#         for i in range(pos,10):
#             if num == 0:
#                 break
#             outCopy[i] = 1

#             self._readBinaryWatch(num - 1, result, i+1, out = list(outCopy))
#             outCopy[i] = 0
        
        
            
#     def binToTime(self, binList):
#         hour = binList[:4][::-1]
#         minute = binList[4:][::-1]
        
#         hour = self.arrToBinStr(hour)
#         minute = self.arrToBinStr(minute)
        
#         hour = str(int(hour,2)%12)
#         minute = str(int(minute, 2))
#         if len(minute) == 1:
#             minute = '0'+minute
        
#         return ":".join([hour,minute])
        
#     def arrToBinStr(self, arr):
#         res = []
#         for el in arr:
#             res.append(str(el))
        
#         return "".join(res)


# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         lenNums = len(nums)
#         if lenNums == 0:
#             return 0
#         if lenNums == 1:
#             if nums[0] == k:
#                 return 1
#             else:
#                 return 0
#         sumMap = {}
#         sumMap[0] = 1
#         count = 0
#         thisSum = 0
#         for i in range(0, lenNums-1):
#             thisSum += nums[i]
#             if thisSum not in sumMap:
#                 sumMap[thisSum] = 0
#             sumMap[thisSum] += 1

#             if thisSum - k in sumMap:
#                 count += sumMap[thisSum -k]

#             return count

# class Solution:
#     def countSubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         arr = []
#         for idx in range(0, len(s)):
#             arr.append(self.palindromsFromLocation(idx, s))
#         return sum(arr)
    
#     def palindromsFromLocation(self, idx,s, size = 1):
#         num = 0
#         if size == 1:
#             num += 1
#             return num + self.palindromsFromLocation(idx,s, size + 1)
            
#         if size == 2 and idx+1 < len(s):
#             if s[idx:idx+2] == s[idx:idx+2][::-1]:
#                 num += 1
#             return num + self.palindromsFromLocation(idx, s, size + 1)
        
#         if size % 2 == 1:
#             print(idx)
#             print(size)
#             if idx+size-2 < len(s) and idx - size+2 >= 0:
#                 if s[idx-size+2:idx+size] == s[idx-size+2:idx+size][::-1]:
#                     print(s[idx-size:idx+size])
#                     return num + 1 + self.palindromsFromLocation(idx,s, size+1)
#                 else:
#                     return num
#             else:
#                 return num
#         else:
#             if idx+size-2 < len(s) and idx - size + 1 >=0:
#                 if s[idx-size+1:idx+size] == s[idx-size+1:idx+size][::-1]:
#                     print(s[idx-size:idx+size])
#                     return num + 1 + self.palindromsFromLocation(idx,s, size+1)
#                 else:
#                     return num
#             else:
#                 return num
#         return num

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2
        
        
        left, right = self.checkIfMultiple( mid, nums)
        print(left)
        if not left and not right:
            return nums[mid]
        
        notFound = True
        while notFound:
            midLeft = len(left)//2
            midRight = len(right)//2
            
            if len(left) > 0:
                leftLeft, rightLeft = self.checkIfMultiple(midLeft, left)
                
                if not leftLeft and not rightLeft:
                    return left[midLeft]
            
            if len(right) > 0:    
                leftRight, rightRight = self.checkIfMultiple(midRight, right)
                
                if not leftRight and not rightRight:
                    return right[midRight]
                
            
    def checkIfMultiple(self, mid, nums):
        if mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
            left = nums[:mid]
            right = nums[mid+2:]
        elif mid - 1 >= 0 and nums[mid] == nums[mid -1]:
            left = nums[:mid-1]
            right = nums[mid+1:]
        else:
            left = None
            right = None
            
        return (left, right)

sol = Solution()
print(sol.singleNonDuplicate([1,1,2]))