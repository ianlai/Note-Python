class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        
        size = len(nums)
        halfsize = size // 2
        map = {}
        for e in nums:
            if e in map:
                map[e] += 1
            else:
                map[e] = 1 
            if map[e] > halfsize:
                return e
        