class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) < 3: 
            return -1
        nums.sort()
        ans = sys.maxsize
        
        for idx in range(len(nums)-2):
            start, end = idx + 1, len(nums) - 1
            while start < end: 
                sum = nums[idx] + nums[start] + nums[end]
                if sum == target: 
                    return sum
                elif sum > target:
                    end -= 1
                else:
                    start += 1
                if abs(ans - target) > abs(sum - target): #update ans
                    ans = sum
        return ans
            
                    
        
        