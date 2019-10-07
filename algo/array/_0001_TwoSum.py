class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0: 
            return None
        numsdict = {}  #<target - nums, index> 
        
        for i in range(len(nums)):
            if nums[i] in numsdict.keys():
                return [i, numsdict[nums[i]]]
            else:
                numsdict[target-nums[i]] = i
        return None
            