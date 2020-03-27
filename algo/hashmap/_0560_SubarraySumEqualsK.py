class Solution:
    
    # Method-3: Use map to record the occurance of each sum  [O(n), 80%]
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        count = 0
        sum = 0 
        sumMap = {0:1} # 0:1 is for counting the case that sum[0:j] equals to k 
                       # other new added ones are for the case that sum[i:j] equals to k
        
        for i in range(len(nums)):
            sum += nums[i]
            
            #Step1: 
            #check whether map has "sum-k" 
            #if yes, count add on the occurance of sum-k
            target = sum - k 
            #(long)
            # if target in sumMap:
            #     count += sumMap[target]
                #print(" sumMap[target]:", sum, "-", k, "->", sumMap[target])
            count += sumMap.get(target, 0)
            
            #Step2:
            #add current sum into map
            # (long)
            # if sum in sumMap:
            #     sumMap[sum] += 1
            # else:
            #     sumMap[sum] = 1 
            # (short)
            sumMap[sum] = sumMap.get(sum, 0) + 1
            
            #print(i, sumMap)
        return count 
    
    # Method-2: Use list to record sum(i,j)  [O(n2), TLE]
    # sum(i, j) = sum(0, j) - sum(0, i) + nums[i]
    def subarraySum_list(self, nums: List[int], k: int) -> int:
        def sumUp(i, j):
            return sumToIdx[j] - sumToIdx[i] + nums[i]
        if len(nums) == 0:
            return 0
        
        # === prepare the cache (list) ===
        sumList = [nums[0]]
        for i in range(1, len(nums)):
            sumList.append(sumList[i-1] + nums[i])
        print(sumList)
        
        # === sum up ===
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sumList[j] - sumList[i] + nums[j] == k:
                    #print("i,j = ", i, j)
                    count += 1
        return count
    
    # Method-1: Use map to record sum(i,j)  [O(n2), TLE]
    # sum(i, j) = sum(0, j) - sum(0, i) + nums[i]
    def subarraySum_map(self, nums: List[int], k: int) -> int:
        def sumUp(i, j):
            return sumToIdx[j] - sumToIdx[i] + nums[i]
        if len(nums) == 0:
            return 0
        
        # === prepare the cache ===
        sumToIdx = {}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sumToIdx[i] = sum
        #print(sumToIdx)
        
        # === sum up ===
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sumUp(i, j) == k:
                    #print("i,j = ", i, j)
                    count += 1
        return count