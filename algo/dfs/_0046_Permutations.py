from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        used = [0] * len(nums) 
        self.dfs(nums, ans, [], 0, used)
        return ans
    
    def dfs(self, nums, ans, cur, index, used):
        if len(cur) == len(nums):
            ans.append(cur)
            return
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                self.dfs(nums, ans, cur + [nums[i]], i, used)
                used[i] = 0
        return 

s = Solution()
arr = [2,3,1,1,2,1]
ans = s.permute(arr)
ans.sort()
for i in range(len(ans)):
    print(i + 1, ans[i])