class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        map = {}
        for e in nums:
            if e in map:
                return True
            else:
                map[e] = 1 
        return False