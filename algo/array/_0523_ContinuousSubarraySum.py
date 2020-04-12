class Solution:

    # Modular substraction: O(n) (95%)
    # (A - B) mod C = (A mod C - B mod C) mod C
    # nums[0:i+1] mod k => x
    # nums[0:j+1] mod k => x
    # nums[i+1:j+1] mod k => x - x = 0 
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        mp = {}
        total = nums[0]
        if k != 0:
            mp[abs(total % k)] = 0 
        for i in range(1, len(nums)):
            #print(mp)
            total += nums[i]
            
            #special case: if we have a subsum = 0 (len > 1), then it can always time 0 to be n * k 
            if nums[i] == 0 and nums[i-1] == 0:  
                return True 
            if k != 0:
                if total % k == 0:  #sum of 0 to i is n *k  
                    return True
                rem = abs(total % k) 
                if rem in mp and i - mp[rem] > 1: #find j, check the i and j are not neighbor
                    return True
                if rem not in mp:
                    mp[rem] = i  #we store the index to calculate the i and j indices
        return False
    
    
    # Optimize summing up: O(n2) (20%)
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i+1, len(nums)):
                total += nums[j]
                if k == 0:
                    if total == 0: return True
                else:
                    if total % k == 0: return True
        return False
    
    # Brute force: O(n3)
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total = sum(nums[i:j+1])
                if k == 0:
                    if total == 0: return True
                else:
                    if total % k == 0: return True
        return False