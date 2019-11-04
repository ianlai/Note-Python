class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        counterMax = 0
        counterCur = 0
        for e in nums:
            if e == 1:
                counterCur += 1 
            else:
                counterMax = max(counterCur, counterMax)
                counterCur = 0
        
        counterMax = max(counterCur, counterMax)
        return counterMax