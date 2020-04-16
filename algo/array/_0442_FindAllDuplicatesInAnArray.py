class Solution:
    # Use positive and negative info to store 1 or more than 1 status 
    # [time: O(n); space: O(1); 60%]
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        ans = []
        count = 0
        for e in nums:
            if nums[abs(e)-1] < 0:
                ans.append(abs(e))
            else:
                nums[abs(e)-1] *= -1
            #print(nums)
        return ans