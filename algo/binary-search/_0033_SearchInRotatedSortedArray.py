class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge cases
        if nums is None: 
            return -1
        if len(nums) == 0:
            return -1 
        start = 0
        end = len(nums)-1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        # Binary search loop 
        while start + 1 < end:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return mid 
            if nums[mid] > nums[start]:
                if nums[start] <= target <= nums[mid]: 
                    end = mid
                else:
                    start = mid 
            if nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]: 
                    start = mid
                else:
                    end = mid 
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
            
            
            
        