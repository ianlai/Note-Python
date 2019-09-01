class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        
        # For edge cases (no rolation)
        m = nums[start]
        if nums[end] < m:
            m = nums[end]
            
        while start + 1 < end: 
            mid = int((start+end)/2)
            if nums[mid] > nums[start]:
                start = mid 
            elif nums[mid] < nums[end]:
                end = mid 
                
        if nums[start] < nums[end] and nums[start] < m:
            return nums[start]
        if nums[start] > nums[end] and nums[end] < m:
            return nums[end]
        
        return m
    