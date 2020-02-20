class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        L, R = 0, 0 
        
        for R in range(len(nums)):
            if nums[L] != nums[R]:
                L += 1
                nums[L] = nums[R]
        return L + 1