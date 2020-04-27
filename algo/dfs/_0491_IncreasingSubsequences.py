class Solution:
    
    # Backtracking [20%]
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return []
        
        #nums.sort()
        used = [0] * len(nums)
        ans = set([])  #use set to remove the duplicates
 
        self.dfs(nums, ans, [], 0, used)
        # print(ans)
        return list(ans)  #change set back to list 
    
    def dfs(self, nums, ans, cur, index, used):
        # print(cur)
        if len(cur) >= 2:
            ans.add(tuple(cur))  #list can't be added into set; change list to tuple instead 
            
        for i in range(index, len(nums)):
            if cur and nums[i] < cur[-1]:
                continue
            used[i] = 1
            self.dfs(nums, ans, cur + [nums[i]], i + 1, used)
            used[i] = 0