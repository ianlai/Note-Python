class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 0 element
        if nums is None or len(nums) == 0:
            return -1
        # 1 element
        if len(nums) == 1:
            return 0
        # peak at the beginning 
        if nums[0] > nums[1]:
            return 0
        # peak at the end
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        start = 0 
        end = len(nums) - 1
        # peak at other position
        while start + 1 < end:
            mid = int((start + end)/2)
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                end = mid
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            else:
                start = mid   #if find a valley, try the later part
        