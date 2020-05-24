class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        total = sum(nums)
        sumLeft = 0
        for i in range(len(nums)):
            if total - nums[i] == 2 * sumLeft:
                return i
            sumLeft += nums[i]
        return -1