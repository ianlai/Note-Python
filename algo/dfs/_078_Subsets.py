class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
        