class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        #select nums[0]
        temp11 = nums[0]
        temp12 = nums[0]
        temp13 = temp12
        for i in range(2, len(nums)-1): #skip the last 
            temp13 = max(temp11 + nums[i], temp12)
            temp11 = temp12
            temp12 = temp13
            
        
        #not select nums[0]
        temp21 = 0
        temp22 = nums[1]
        temp23 = temp22
        for i in range(2, len(nums)): #until the last 
            temp23 = max(temp21 + nums[i], temp22)
            temp21 = temp22
            temp22 = temp23
        
        print("    select nums[0]:", temp13)
        print("not select nums[0]:", temp23)
        
        return max(temp13, temp23)