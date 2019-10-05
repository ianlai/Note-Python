class Solution:
    
    #=============================================================
    # Binary Search for findFirst, findLast (cleaner)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]
        first = self.findFirst(nums, target) 
        last  = self.findLast(nums, target)
        return [first, last]
    def findFirst(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid 
            elif nums[mid] < target:
                start = mid 
            else:
                end = mid 
        if nums[start] == target:  #order matters
            return start 
        if nums[end] == target:
            return end
        return -1 
    def findLast(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid 
            elif nums[mid] < target:
                start = mid 
            else:
                end = mid 
        if nums[end] == target:   #order matters
            return end
        if nums[start] == target:  
            return start 
        return -1 

    #=============================================================
    # Binary Search Then Linear Search 
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1,-1]
        
        start, end = 0, len(nums)-1
        
        ### Binary search 
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                break
            elif nums[mid] > target:
                end = mid 
            elif nums[mid] < target:
                start = mid 
        #print("start, end:", start, end)
        
        ### Binary search edge case 
        index = 0 
        if nums[start] == target: 
            index = start 
        elif nums[end] == target:
            index = end
        else:
            return [-1, -1]
        #print("index:", index)
        
        ### Find the leftmost and right most indexes
        left, right = index, index
        while True:
            if left > 0 and nums[left-1] == nums[left]:
                left -= 1
            elif right < len(nums)-1 and nums[right] == nums[right+1]:
                right += 1
            else:
                return [left, right]