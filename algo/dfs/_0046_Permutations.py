from typing import List
class Solution:
    
    # Passing cur+[] to generate new list when calling dfs() each time
    def permute1(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        used = [0] * len(nums) 
        self.dfs(nums, ans, [], 0, used)
        print(ans)
        return ans
    
    def dfs1(self, nums, ans, cur, index, used):
        if len(cur) == len(nums):
            ans.append(cur)
            return
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                self.dfs(nums, ans, cur + [nums[i]], i, used)
                used[i] = 0
        return 
    
    # Passing cur directly and copy result when generating each answer 
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        used = [0] * len(nums) 
        self.dfs(nums, ans, [], 0, used)
        return ans
    
    def dfs(self, nums, ans, cur, index, used):
        if len(cur) == len(nums):
            #we need to generate a new copy
            #otherwise the element will be removed after jumping out of the function
            ans.append(cur.copy())  
            return
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                cur.append(nums[i])
                self.dfs(nums, ans, cur, i, used)
                cur.remove(nums[i])
                used[i] = 0
        return 

s = Solution()
arr = [2,3,1,1,2,1]
ans = s.permute(arr)
ans.sort()
for i in range(len(ans)):
    print(i + 1, ans[i])