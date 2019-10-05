from typing import List

class Solution:
    def searchAny(self, nums: List[int], target: int) -> int:
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

    def searchFirst(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==0: 
            return -1
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                end = mid 
            elif target < nums[mid]:
                end = mid
            else: 
                start = mid
        
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1
    
    def searchLast(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==0: 
            return -1
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                start = mid 
            elif target < nums[mid]:
                end = mid
            else: 
                start = mid
        
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1
    
s = Solution()
nums = [1,2,2,3,3,3,3,3,9] 
target = 3 
print("Find", target, "in", nums, "(any)  : ", s.searchAny(nums, target))
print("Find", target, "in", nums, "(first): ", s.searchFirst(nums, target))
print("Find", target, "in", nums, "(last) : ", s.searchLast(nums, target))

target = 4
print("Find", target, "in", nums, "(any)  : ", s.searchAny(nums, target))
print("Find", target, "in", nums, "(first): ", s.searchFirst(nums, target))
print("Find", target, "in", nums, "(last) : ", s.searchLast(nums, target))

                
            