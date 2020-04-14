class Solution:
    
    # Two Pointer [O(n), 88%]
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        n = len(height)
        volumn = 0 
        left, right = 0, n-1
        while left < right:
            width = right - left 
            curHeight = 0
            if height[left] <= height[right]:
                curHeight = height[left]
                left += 1
            else:
                curHeight = height[right]
                right -= 1
            volumn = max(volumn, width * curHeight)
        return volumn
    
    # DP (incorrect)
    # def maxArea(self, height: List[int]) -> int:
    #     if len(height) < 2: 
    #         return 0
    #     n = len(height)
    #     dp = [0] * n  #max volumn before this bar (either include this or not)
    #     dp[0] = 0
    #     tallest = height[0]
    #     tallestIdx = 0
    #     for i in range(1, n):
    #         dp[i] = max(dp[i-1], (i - tallestIdx) * min(tallest, height[i]))
    #         if height[i] > tallest:
    #             tallest = height[i]
    #             tallestIdx = i 
    #     #print(dp)
    #     return dp[-1] 
    
    #Brute Force [O(n2), TLE]
    def maxArea1(self, height: List[int]) -> int:
        if len(height) < 2: 
            return 0
        n = len(height)
        volumn = 0
        for i in range(n):
            for j in range(i+1, n):
                cur = (j - i) * min(height[i], height[j])
                #print(i, j, cur)
                volumn = max(volumn, cur)
        return volumn 