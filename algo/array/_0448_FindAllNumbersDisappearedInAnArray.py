class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        
        cal = [0] * len(nums)
        ans = []
        
        for e in nums:
            cal[e-1] += 1 
        
        for i in range(len(cal)):
            if cal[i] == 0:
                ans.append(i+1)
        
        return ans