class Solution:
    
    # s: searching string, t: target string
    #
    # Use 2 maps to calculate the elements in s and t 
    # Sliding window approach [O(max(S, T), 14%]
    def minWindow(self, s: str, t: str) -> str:
        def hasAllChars(countS, countT):
            #print("hasAllChars: ", countS)
            for e in countT:
                if e not in countS or countS[e] < countT[e]:
                    return False
            return True
        
        if len(s) == 0:
            return ""
        if len(t) == 0:
            return ""
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        
        countS = {}  #count of s
        countT = {}  #count of t          
        ans = [0, None]  #min window, (p1, p2) of the min window
        p1, p2 = 0, 0
        
        for e in t:
            countT[e] = countT.get(e, 0) + 1
        
        # Find the first window in s which contains all chars in t 
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            has = hasAllChars(countS, countT)
            #print("i:", i, "has:", has, count, countT)
            if has:
                p2 = i
                ans[0] = p2 - p1 + 1
                ans[1] = (p1, p2)
                break     

        # Loop until p2 reaches the end of s 
        # p1 move forward if the window contains all chars in t (try to shorter window)
        # p2 move forward if the window doesn't contain all chars in t (try to expand window)
        while True:
            has = hasAllChars(countS, countT)
            if p1 < p2:
                if has:
                    countS[s[p1]] -= 1
                    p1 += 1
                    nowLength = p2 - p1 + 1
                    if nowLength < ans[0] and hasAllChars(countS, countT):
                        ans[0] = nowLength
                        ans[1] = (p1, p2)
                else: 
                    p2 += 1 
                    if p2 >= len(s):
                        break
                    countS[s[p2]] = countS.get(s[p2], 0) + 1
            else:
                p2 += 1
                if p2 >= len(s):
                    break
                countS[s[p2]] = countS.get(s[p2], 0) + 1
                
        if not ans[1]:
            return ""

        return s[ans[1][0]:ans[1][1]+1]
        