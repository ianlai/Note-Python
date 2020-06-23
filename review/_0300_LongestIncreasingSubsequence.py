class Solution:
    
    # Binary Search [O(nlogn), 85%]
    # https://blog.csdn.net/u012505432/article/details/52228945
    # 1. Form a tail array tails[i] which is the smallest element of i-length LIS (tails is ascending)
    # 2. Traverse the nums
    # 3. If the nums[i] is larger than tails[i-1], just assign x to tails[i]
    # 4. If the nums[i] is smaller than tails[i-1], find the min element in tails[] which is larger than x (by BS)
    # 5. Update the min element to be x 
    # 6. Return the last index of tails 
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        print("Binary Search")
        if nums is None or len(nums) == 0: 
            return 0
        tails = [nums[0]]
        
        #Traverse nums 
        for i in range(1, len(nums)):
            
            start, end = 0, len(tails) - 1
            x = nums[i]
            #print("-----", x, "-----")
            
            #Edge cases (not necessary)
            # if x < tails[0]:
            #     tails[0] = x
            #     #print("e1:", i)
            #     print(x, ":", tails, "e1")
            #     continue
            # elif x > tails[-1]:
            #     tails.append(x)
            #     #print("e2:", i)
            #     print(x, ":", tails, "e2")
            #     continue
                
            #Binary Search (find an interval)
            while start + 1 < end:
                mid = (start + end) // 2
                if tails[mid-1] <= x <= tails[mid]: #target 
                    tails[mid] = x  #update the tail which is min and larger than x 
                    start = mid 
                    end = mid
                    break
                elif x > tails[mid]:
                    start = mid
                elif x < tails[mid-1]:
                    end = mid
                    
            #Edge cases for binary search 
            if x <= tails[start]:
                tails[start] = x
            elif tails[start] < x <= tails[end]:
                tails[end] = x
            else:
                tails.append(x)
        
            #print(tails)
            
        return len(tails)
        
    #=========================================
    
    # DP [O(n2), 29%] 
    def lengthOfLIS2(self, nums: List[int]) -> int:
        print("DP")
        if nums is None or len(nums) == 0: 
            return 0
        lis = [1] * len(nums) 
        
        # Form the lis array 
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: 
                    lis[i] = max(lis[j] + 1, lis[i]) 
                
        return max(lis)
            
        