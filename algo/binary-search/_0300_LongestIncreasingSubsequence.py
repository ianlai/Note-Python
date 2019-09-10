class Solution:
    
    # Binary Search: nlogn 
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        tails = [0]
        tails[0] = nums[0]
        
        for i in range(1, len(nums)):
            start, end = 0, len(tails)-1
            x = nums[i]
            #print("-----", x, "-----")
            
            #Edge cases
            # if x <= tails[0]:
            #     tails[0] = x
            #     #print("e1:", i)
            #     #print(tails)
            #     continue
            # #elif x > tails[i-1]:
            # elif x > tails[-1]:
            #     #tails[i] = x 
            #     tails.append(x)
            #     #print("e2:", i)
            #     #print(tails)
            #     continue
                
            #Binary Search
            while start + 1 < end:
                mid = (start + end) // 2
                #print(start, "-", mid, "-", end)
                if tails[mid-1] <= x <= tails[mid]:
                    tails[mid] = x
                    start = mid 
                    end = mid
                    #print("bs:", mid)
                    break
                elif x > tails[mid]:
                    start = mid
                elif x < tails[mid-1]:
                    end = mid
                    
            #Edge cases for binary search 
            if x <= tails[start]:
                tails[start] = x
                #print("e4:", start)
            elif tails[start] < x <= tails[end]:
                tails[end] = x
                #print("e5:", end)
            else:
                tails.append(x)
            
            #print(tails)
            
        return len(tails)
        
    
    # DP: n^2
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        lis = [1] * len(nums) 
        
        # (1) Form the lis array 
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: 
                    lis[i] = max(lis[j] + 1, lis[i]) 
                # else:
                #     lis[i] = lis[j]  #wrong!  
        
        #print(lis)
        
        # (2) Get the max in lis array
        lisNum = 0 
        for e in lis:
            if e > lisNum:
                lisNum = e
                
        return lisNum
            
        