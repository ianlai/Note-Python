class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort = sorted(nums)
        left, right = 0, len(nums)-1
        
        # Find left change
        for i in range(len(nums)):
            if nums[i] != sort[i]:
                left = i
                break
                
        # Find right change 
        for i in range(len(nums)-1, 0, -1):
            if nums[i] != sort[i]:
                right = i
                break
        
        # Judge the case is sorted or not
        ans = right - left + 1 
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return ans        
        return 0