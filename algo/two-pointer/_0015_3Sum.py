class Solution():
    
    # Two pointer approach (fast)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return None
        
        nums.sort()
        #print(nums)
        ans = []
        
        for i in range(len(nums)-2):
            target = nums[i]
            if target > 0: #skip the positive target (speed up 20%)
                break   
            if i > 0 and target == nums[i-1]:  #skip the redunduncy of target
                continue
            p, q = i + 1, len(nums) - 1
            while p < q:
                if p > i+1 and nums[p-1] == nums[p]:  #skip the redunduncy of nums[p]
                    p += 1
                    continue
                if q < len(nums) - 1 and nums[q] == nums[q+1]: #skip the redunduncy of nums[q]
                    q -= 1
                    continue
                sum = target + nums[p] + nums[q] 
                if sum == 0:
                    ans.append([target, nums[p], nums[q]])
                    p += 1
                    q -= 1
                elif sum > 0:
                    q -= 1
                elif sum < 0:
                    p += 1
        return ans

    #Hash map approach (slow)
    def threeSum_hashmap(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return None
        
        nums.sort()
        print(nums)
        ans = []
        map = {}
            
        for i in range(len(nums)):
            target = -nums[i]
            #print("-target:" + str(target))
            if i > 0 and target == -nums[i-1]:
                #print("-c") 
                continue
            for j in range (i+1, len(nums)):
                n1 = nums[j]
                #print("--n1:" + str(n1))
                if j >= i+2 and n1 == nums[j-1]:
                    #print( "--c") 
                    continue
                map[target - n1] = 1
                for k in range(j+1, len(nums)):
                    n2 = nums[k]
                    #print("--n2:" + str(n2))
                    if k >= j+2 and n2 == nums[k-1]:
                        #print( "---c") 
                        continue
                    
                    if n2 in map:
                        #print([-target, n1, n2])
                        ans.append([-target, n1, n2])
                map = {}  #reset (in the 3rd loop)

        return ans