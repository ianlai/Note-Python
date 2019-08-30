class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
                # end = mid - 1 (ok)
            else: 
                start = mid
                # start = mid + 1 (ok)
        
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
 
        return -1
                
            