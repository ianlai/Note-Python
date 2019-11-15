class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        pget, pput = 0, 0 
        for pget in range(len(nums)):
            if nums[pget] == val:
                continue
            else:
                nums[pput] = nums[pget]
                pput += 1
        
        return pput