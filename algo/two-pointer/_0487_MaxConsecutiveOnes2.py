class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        subArr = []
        s, e = -1, -1 
        for i in range(len(nums)):
            if i-1 < 0 and nums[i-1] == 1:
                s = 0 
            if nums[i-1] == 0 and nums[i] == 1:
                s = i
            if nums[i-1] == 1 and nums[i] == 0 and s != -1:
                e = i-1
            if i == len(nums) - 1 and nums[i] == 1:
                e = i
            if s != -1 and e != -1:
                subArr.append((s,e))
                s, e = -1, -1
                
        if len(subArr) == 0:
            return 1
        print(subArr)
        
        # From subArr
        mx = 0        
        for i in range(1, len(subArr)):
            if subArr[i][0] - subArr[i-1][1] == 2:
                mx = max(mx, subArr[i][1] - subArr[i-1][0] + 1)
            if subArr[i][0] - subArr[i-1][1] > 2:
                mx = max(mx, subArr[i-1][1] - subArr[i-1][0] + 1 + 1)
                mx = max(mx, subArr[i][1] - subArr[i][0] + 1 + 1)
            #mx = max(mx, subArr[-1][1] - subArr[-1][0] + 1)
        
        # Specail case: one subarray 
        if len(subArr) == 1:
            if subArr[0][1] != len(nums) -1 or subArr[0][0] != 0:
                mx = max(mx, subArr[0][1] - subArr[0][0] + 1 + 1)
            else:
                mx = max(mx, subArr[0][1] - subArr[0][0] + 1)
        
        return mx
                
            