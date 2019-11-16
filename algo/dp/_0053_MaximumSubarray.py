class Solution:
    #3 solutions: O(n3), O(n2), O(n)
    
    # Time=O(n) ; Space=O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0 :
            return 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        return max(dp)