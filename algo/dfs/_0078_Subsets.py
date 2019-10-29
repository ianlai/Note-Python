from typing import List
import time
class Solution:
    
    # DFS (backtracking) 
    # Implicit Graph: What I can select for the next?
    def subsetsBacktracking(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        
        ans = []
        self.dfs(nums, [], 0, ans)
        return ans
    
    def dfs(self, nums, cur, index, ans):
        ans.append(cur)
        for i in range(index, len(nums)):
            self.dfs(nums, cur + [nums[i]], i + 1, ans)
    # ======================================================
    # DFS 
    # Implicit Graph: Whether I should select the next? 
    def subsetsDFS(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        self.dfs2(nums, ans, [], 0)
        return ans
    
    def dfs2(self, nums, ans, curArr, index):
        if index == len(nums):
            ans.append(curArr)
            return
        self.dfs2(nums, ans, curArr+[nums[index]], index+1)
        self.dfs2(nums, ans, curArr, index+1)
        return
    # ======================================================
    # Double
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
            ansArr.extend(newArr)
            #print("ansArr:", ansArr)
        return ansArr


s = Solution()
nums1 = [1,2,3]
# print("DFS   :", s.subsetsDFS(nums1))
# print("Double:", s.subsetsDouble(nums1))


nums2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# Time measurment 

t1_s = time.process_time_ns()
s.subsetsBacktracking(nums2)
t1_e = time.process_time_ns()
print("Time elapsed - Backtracking   (ms)", (t1_e - t1_s)/1000000) # CPU seconds elapsed (floating point)

t2_s = time.process_time_ns()
s.subsetsDFS(nums2)
t2_e = time.process_time_ns()
print("Time elapsed - DFS            (ms)", (t2_e - t2_s)/1000000) # CPU seconds elapsed (floating point)

t3_s = time.process_time_ns()
s.subsetsDouble(nums2)
t3_e = time.process_time_ns()
print("Time elapsed - Double         (ms)", (t3_e - t3_s)/1000000) # CPU seconds elapsed (floating point)
