class Solution:
    
    # When all the count elements have a common factors greater than 1 -> True 
    # To find the common factor, we need to use GCD 
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck:
            return False
        
        ### Count the elements 
        mp = {}
        for e in deck:
            mp[e] = mp.get(e, 0) + 1
        
        ### Convert map to list 
        count = [mp[k] for k in mp]
        
        if len(count) == 1:
            return count[0] > 1
        
        # count.sort()
        
        ### Find common factor
        print("Count:", count)
        p1 = count[0]
        p2 = count[1]
        print(p1, p2)
        commonFactor = 0
        if p1 == p2:
            commonFactor = p1
        else:
            while p2 != 0:
                if p2 > p1: 
                    p2 = p2 - ((p2 // p1) * p1)
                else:
                    p1, p2 = p2, p1
            commonFactor = p1 
        if commonFactor == 1:
            return False
        print("Common Factor:", commonFactor)
        
        factors = []
        #for i in range(1, math.floor(math.sqrt(commonFactor)) + 1):
        
        ### Find factors 
        for i in range(1, commonFactor + 1):
            if commonFactor % i == 0:
                factors.append(i)
        print("Factors:", factors)
        
        ### Use factors to check the rest of the count values
        for i in range(1, len(factors)):
            fac = factors[i]
            cnt = 0 
            for j in range(len(count)):
                if count[j] % fac == 0:
                    cnt += 1
            if cnt == len(count):
                return True  
        return False
            