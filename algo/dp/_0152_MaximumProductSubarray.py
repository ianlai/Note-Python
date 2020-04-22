class Solution:
    
    # DP approach [O(n), 61%]
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dpmax = [0] * len(nums)
        dpmin = [0] * len(nums)
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        finalMax = nums[0]
        
        # When muliplying a negative num, min will become max, and max will become min
        for i in range(1, len(nums)):
            if nums[i] >= 0 :
                dpmax[i] = max(dpmax[i-1] * nums[i], nums[i])
                dpmin[i] = min(dpmin[i-1] * nums[i], nums[i])
            else:
                dpmax[i] = max(dpmin[i-1] * nums[i], nums[i])
                dpmin[i] = min(dpmax[i-1] * nums[i], nums[i])
            finalMax = max(finalMax, dpmax[i], dpmin[i])
        return finalMax
    
    # ========================================================================
    
    # Separate the segments by 0 and calculates each's max muliple [O(n), 94%]
    def maxProduct1(self, nums: List[int]) -> int:
        if not nums: 
            return 0
    
        # Cut the segments between 0
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
                
        ans = -float('inf')
        while zeros:
            lastZero = zeros[-1]
            
            # Case of no number follows the last zero
            if lastZero == len(nums) -1:
                ans = max(ans, 0)
                nums = nums[:lastZero]
                zeros.pop()
                continue
                
            # Calculate the multiple of the segment follows the last zero 
            curArr = nums[lastZero+1:]
            multiple = self.maxMultiple(curArr)
            ans = max(ans, multiple)
            ans = max(ans, 0)
            nums = nums[:lastZero]
            zeros.pop()
        
        # Calculate the last segment
        multiple = self.maxMultiple(nums)
        ans = max(ans, multiple)
        return ans
    
    def maxMultiple(self, arr):
            if not arr:
                return 0
            if len(arr) == 1 and arr[0] < 0:
                return arr[0]
            
            # Find the first and last negative numbers
            firstNegative, lastNegative = -1, -1
            for i in range(len(arr)):
                if arr[i] < 0: 
                    firstNegative = i 
                    break
            for i in range(len(arr)-1, -1, -1):
                if arr[i] < 0: 
                    lastNegative = i 
                    break
                    
            # Calculate the mutiple of arr
            maxMultiple = 1 
            multiple = 1
            for i in range(len(arr)):
                multiple *= arr[i]
            
            # Calculate the max of multiples 
            if firstNegative == -1 and lastNegative == -1:  #0
                print("0 negative")
                return multiple
            if firstNegative == lastNegative: #1 
                print("1 negative")
                leftMultiple = 1
                rightMultiple = 1
                for i in range(firstNegative):
                    leftMultiple *= arr[i]
                for i in range(firstNegative+1, len(arr), 1):
                    rightMultiple *= arr[i]
                print("left:", leftMultiple)
                print("right:", rightMultiple)
                return max(leftMultiple, rightMultiple)
            else: #More than 1 
                if multiple > 0:
                    print("even negative")
                    return multiple
                print("odd negative")
                leftMultiple  = 1
                rightMultiple = 1
                for i in range(firstNegative+1, len(arr), 1):
                    leftMultiple *= arr[i]
                for i in range(lastNegative-1, -1, -1):
                    rightMultiple *= arr[i]
                return max(leftMultiple, rightMultiple)