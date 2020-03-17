class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: 
            return 
        
        #Trace from back, find the first low point (head) before the dscending subarray 
        head, headIdx = -1, -1 
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                head = nums[i-1]
                headIdx = i-1
                break  
        print(nums)
        
        #Trace from back, find the first point larger than head, swap it with head
        for i in range(len(nums) - 1, headIdx, -1):
            if nums[i] > head:
                nums[i], nums[headIdx] = nums[headIdx], nums[i]
                break
        print(nums)
        
        #Reverse the subarray from head + 1 to the end
        left, right = headIdx + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1 
        print(nums)
        
        return 