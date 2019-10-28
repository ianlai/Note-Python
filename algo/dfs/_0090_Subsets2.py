class Solution:
    # DFS (backtracking)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        
        nums = sorted(nums)  #must
        ans = []
        used = [0] * len(nums)
        self.dfs(nums, [], 0, used, ans)
        return ans
    
    def dfs(self, nums, cur, index, used, ans):
        ans.append(cur)
        for i in range(index, len(nums)):
            # if used[i] == 1:
            #     continue
            if i > 0 and nums[i-1] == nums[i] and used[i-1] is 0:  #remove redundancy
                continue
            used[i] = 1
            self.dfs(nums, cur + [nums[i]], i + 1, used, ans)
            used[i] = 0