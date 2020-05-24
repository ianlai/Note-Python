class Solution:
    
    # O(S) to traverse, each step takes O(26) to compare the counters [15%]
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isSameCounter(counter1, counter2):
            c1 = counter1.copy()
            c2 = counter2.copy()
            for key in list(c1):
                if key not in c2:
                    return False
                if c1[key] != c2[key]:
                    return False
                del c1[key]
                del c2[key]
            return True
        
        if len(s) == 0 or len(p) == 0:
            return []
        lenS, lenP = len(s), len(p)
        counterP = collections.Counter(p)
        counterS = collections.Counter(s[:lenP])
        ans = []
        
        for i in range(lenP, lenS, 1):
            head = i - lenP
            if isSameCounter(counterP, counterS):
                ans.append(head)
            counterS[s[head]] -= 1
            counterS[s[i]] += 1
            
        # Last comparison 
        if isSameCounter(counterP, counterS):
            ans.append(lenS - lenP)
        return ans
    
            
            