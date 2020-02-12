class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None:
            return []
    
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_of_1_2 = nums[i] + nums[j]
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    sum = nums[m] + nums[n] + sum_of_1_2
                    if sum == target:
                        ans.add((nums[i],nums[j],nums[m],nums[n]))  #add tuple instead of list
                        n -= 1
                        m += 1
                    elif sum > target:
                        n -= 1
                    else: 
                        m += 1
        return list(ans) #convert the set back to list