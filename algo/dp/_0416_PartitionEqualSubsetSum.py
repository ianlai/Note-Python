class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        s = sum(nums)
        if s % 2 == 1:
            return False
        ans = self.helper(nums, 0, len(nums)-1, s//2, {})
        return ans

    def helper(self, nums, start, end, target, memo):
        if start > end:
            return False
        
        # if (start, end, target) in memo:
        #     return memo[(start, end, target)]
        if target in memo:
            return memo[target]

        if target < 0 :
            #memo[(start, end, target)] = False
            memo[target] = False
            return False 
        if target == 0:
            # memo[(start, end, target)] = True
            memo[target] = True
            return True

        if self.helper(nums, start+1, end, target-nums[start], memo):
            memo[target] = True
            return True
        if self.helper(nums, start, end-1, target-nums[end], memo):
            memo[target] = True
            return True
        if self.helper(nums, start+1, end-1, target, memo):
            memo[target] = True
            return True
        memo[target] = False
        return False