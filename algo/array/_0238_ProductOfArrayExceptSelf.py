class Solution:
    
    # Use ans array instead of creating 2 arrays beforehand; without division [time: O(n), 66% ; space: O(1)]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        n = len(nums)
        ans = [0] * n
        
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        #print(ans)
        
        R = 1
        for i in range(n-2, -1, -1):
            R = R * nums[i+1]
            ans[i] = ans[i] * R
        #print(ans)    
        return ans
    
    # Form 2 multiple arrays; without division [time: O(n), 48% ; space: O(n)]
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        n = len(nums)
        mulLeft  = [0] * n 
        mulRight = [0] * n
        ans      = [0] * n
        
        cur = 1
        for i in range(n):
            cur *= nums[i]
            mulLeft[i] = cur
        
        cur = 1
        for i in range(n-1, -1, -1):
            cur *= nums[i]
            mulRight[i] = cur
            
        ans[0], ans[-1] = mulRight[1], mulLeft[-2]
        for i in range(1, n-1, 1):
            ans[i] = mulLeft[i-1] * mulRight[i+1]
            
        # print(mulLeft)
        # print(nums)
        # print(mulRight)
        # print(ans)
            
        return ans
        
            