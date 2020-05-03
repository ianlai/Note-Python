class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        # Edge cases
        if not nums:
            return -1 
        
        start, end = 0, len(nums) - 1
        
        # Not necessary to have this edge cases: 
#         if nums[start] == target:
#             return start
        
#         if nums[end] == target:
#             return end
        
        # Binary search loop 
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid 
            if nums[start] < nums[mid]:    #left part 
                if nums[start] <= target <= nums[mid]:  #equal is necessary
                    end = mid
                else:
                    start = mid 
            elif nums[mid] < nums[end]:    #right part
                if nums[mid] <= target <= nums[end]:   #equal is necessary
                    start = mid
                else:
                    end = mid 
                    
        # Binary search check 
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
            
            
            
        