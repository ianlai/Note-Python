class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid 
            else:
                end = mid 
        
        if target <= nums[start]: 
            return start
        elif nums[start] < target <= nums[end]: 
            return end
        elif target > nums[end]:
            return end + 1
