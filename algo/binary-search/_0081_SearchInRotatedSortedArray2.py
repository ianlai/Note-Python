class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Edge cases
        if nums is None or len(nums) == 0:
            return False
        
        # mset = set(nums)
        # nums = list(mset)
        
        start, end = 0, len(nums)-1
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        
        # Preprocess (remove redundants in two ends)
        while start < end and nums[start] == nums[end]:
            start += 1
        
        # Binary search loop 
        while start + 1 < end:
            mid = (start + end) // 2
            #print(start, mid, end)
            if target == nums[mid]:
                return True 
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]: 
                    end = mid
                else:
                    start = mid 
            if nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]: 
                    start = mid
                else:
                    end = mid 
                    
        # Binary search check 
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        
        return False