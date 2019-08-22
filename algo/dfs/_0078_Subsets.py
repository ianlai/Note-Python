from typing import List
import time

class Solution:
    def subsetsDFS(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        self.dfs(nums, ans, [], 0)
        return ans
    def dfs(self, nums, ans, curArr, index):
        if index == len(nums):
            ans.append(curArr)
            return
        self.dfs(nums, ans, curArr+[nums[index]], index+1)
        self.dfs(nums, ans, curArr, index+1)
        return
    
    def subsetsDouble(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ansArr = []
        ansArr.append([])
        ansArr.append([nums[0]])
        #print(ansArr)
        for i in range(1, len(nums)):
            #newArr = ansArr[:]  #new list (but only 1 layer)
            newArr = [cur[:] for cur in ansArr] #new list
            #print("newArr:", newArr)
            for cur in newArr:
                cur.append(nums[i])

            #ansArr.extend(newArr)  #combine 2 lists (ok)
            ansArr += newArr        #combine 2 lists (ok)
            #print("ansArr:", ansArr)
        return ansArr


s = Solution()
nums1 = [1,2,3]
print("DFS   :", s.subsetsDFS(nums1))
print("Double:", s.subsetsDouble(nums1))


nums2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Time measurment 
t1_s = time.process_time_ns()
s.subsetsDFS(nums2)
t1_e = time.process_time_ns()

t2_s = time.process_time_ns()
s.subsetsDouble(nums2)
t2_e = time.process_time_ns()

print("Time elapsed - DFS    (ms)", (t1_e - t1_s)/1000000) # CPU seconds elapsed (floating point)
print("Time elapsed - Double (ms)", (t2_e - t2_s)/1000000) # CPU seconds elapsed (floating point)
