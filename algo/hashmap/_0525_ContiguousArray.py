class Solution:
    
    # Traverse 1: Calculate the diffs between 0 and 1 
    # Traverse 2: Calculate the furest indices in each diffs 
    # [O(n), 13%]
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        cnt = []  #how much 0 more than 1 
        if nums[0] == 0: 
            cnt.append(1)  
        else:
            cnt.append(-1)
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                cnt.append(cnt[i-1] + 1)
            if nums[i] == 1:
                cnt.append(cnt[i-1] - 1)
        print(cnt)
        
        cntToIdx = {0:-1}  #count number to its first index
        totalLength = 0
        for i in range(len(nums)):
            if cnt[i] in cntToIdx: 
                length = i - cntToIdx[cnt[i]]
                totalLength = max(length, totalLength)
            else:
                cntToIdx[cnt[i]] = i
        return totalLength
        
    # Brute force  [O(n2), TLE]
    def findMaxLength1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cnt = {0:0, 1:0}
        longest = 0
        for i in range(len(nums)):
            cnt = {0:0, 1:0}
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    cnt[0] = cnt.get(0, 0) + 1
                if nums[j] == 1: 
                    cnt[1] = cnt.get(1, 0) + 1
                if cnt[0] == cnt[1]:
                    longest = max(longest, cnt[0])
                #print(i, j, " - ", cnt[0], cnt[1], " - ", longest)
     
        return longest * 2