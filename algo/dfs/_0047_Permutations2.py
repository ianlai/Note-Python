class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        mset = set()
        ans = []
        used = [0] * len(nums) 
        self.dfs(nums, mset, [], 0, used)
        ans = list(mset)
        return ans
    
    def dfs(self, nums, mset, cur, index, used):
        if len(cur) == len(nums):
            mset.add(tuple(cur))  #list cannot be added to a set directly 
            return
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                self.dfs(nums, mset, cur + [nums[i]], i, used)
                used[i] = 0
        return 