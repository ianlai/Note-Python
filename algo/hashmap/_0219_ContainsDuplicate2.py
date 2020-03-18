class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums is None or len(nums) == 0:
            return False
        
        map = {} #value, index
        
        #First scan (list)
        for i in range(len(nums)):
            if nums[i] in map:
                idxArr = map[nums[i]]
                idxArr.append(i)
            else:
                map[nums[i]] = [i]  
        print(map)
        
        #Second scan (map)
        for e in map:
            idxArr = map[e]
            if len(idxArr) == 1:  #special case (based on definition)
                continue
            #print(e, idxArr)
            minDistance = float('Inf')
            distance = 0 
            for i in range(1, len(idxArr)):
                distance = idxArr[i] - idxArr[i-1]
                minDistance = min(minDistance, distance)
                    
            #compare in the end of one loop
            if minDistance <= k:
                return True
                
        return False