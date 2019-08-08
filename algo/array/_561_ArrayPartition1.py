class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        sum = 0
        for i in range(1, len(nums),2):
            sum += min(nums[i-1], nums[i])
        return sum