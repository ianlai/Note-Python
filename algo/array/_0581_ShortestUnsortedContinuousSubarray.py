class Solution:
    
    # Two pointers [96%]
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                left = i - 1
                break
            left = i
        print("left:", left, " right:", right )
                
        if(left >= right): #sorted
            return 0
        
        for j in range(len(nums)-2, -1, -1):
            if nums[j] > nums[j+1]:
                right = j + 1
                break
            right = j 
        print("left:", left, " right:", right )
        
        minVal = min(nums[left:right+1])
        maxVal = max(nums[left:right+1])

        print("min, max:", minVal, maxVal)
        while left >= 0: 
            if nums[left] > minVal: 
                left -= 1
            else:
                break
        while right <= len(nums)-1:
            if nums[right] < maxVal: 
                right += 1
            else:
                break

        print("l, r:", left, right)
        return right - left - 1
        
    #===============================================
    # Sorting [85%]
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort = sorted(nums)
        i, j = 0, len(nums)-1
        left, right = 0, len(nums)-1
        
        # Find left change
        while i < len(nums) and nums[i] == sort[i]:
            i += 1
                
        # Find right change 
        while j >= i and nums[j] == sort[j]:
            j -= 1
        
        print(i, j)
        return j - i + 1   
    
    #===============================================
    # Sorting
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort = sorted(nums)
        left, right = 0, len(nums)-1
        
        # Find left change
        for i in range(len(nums)):
            if nums[i] != sort[i]:
                left = i
                break
                
        # Find right change 
        for i in range(len(nums)-1, 0, -1):
            if nums[i] != sort[i]:
                right = i
                break
        
        # Judge the case is sorted or not
        ans = right - left + 1 
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return ans        
        return 0