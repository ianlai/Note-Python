class Solution:
    # Two pointers: reuse the sum
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: 
            return 0
        
        minSize = float("inf")         #initialize 
        start, end = 0, 0 
        sum = nums[0]
        while end < len(nums) :
            #print("s:", start, " e:", end, " sum:", sum, " minSize:", minSize)
            if sum < s:
                end += 1
                if end == len(nums):
                    break
                sum += nums[end]
            else: 
                minSize = min(minSize, end - start + 1)
                sum -= nums[start]
                start += 1
                
        if minSize == float("inf"):
            return 0
        else: 
            return minSize
        
    #-------------------------------------------------
    
    # One pointer: re-calculate the sum everytime (TLE)
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: 
            return 0
        
        minSize = float("inf")         #initialize 
        for start in range(len(nums)-1):
            #print(start)
            sum = 0
            next = start
            while True:
                if next == len(nums):  #fail
                    break
                sum += nums[next]
                #print(" >", " next:", next, " sum:", sum)
                if sum >= s:           #success
                    size = next - start + 1 
                    minSize = min(minSize, size)
                    #print(" *", " minSize:", minSize)
                    break 
                next += 1
                
        if minSize == float("inf"):
            return 0
        else: 
            return minSize