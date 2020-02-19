class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return 
        
        countArr = [0,0,0]
        
        #count
        for e in nums:
            countArr[e] += 1
        print(countArr)
        
        #fill in 
        index = 0
        for i in range(3):
            count = countArr[i]
            for _ in range(count):
                nums[index] = i
                index += 1
        return 
                