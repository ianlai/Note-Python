class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return nums
        
        dst = 0
        
        for src in range(len(nums)):
            if nums[src] == 0:
                continue
            else:
                nums[dst] = nums[src]
                dst += 1
        
        while dst <= len(nums) - 1:
            nums[dst] = 0
            dst += 1