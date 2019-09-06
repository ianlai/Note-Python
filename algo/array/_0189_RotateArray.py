class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # leftReversedArr  = nums[-k-1::-1]
        # rightReversedArr = nums[:-k-1:-1]
        # temp = leftReversedArr + rightReversedArr
        # nums = temp[::-1]
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1-k)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        
    def reverse(self, nums, start, end):
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1