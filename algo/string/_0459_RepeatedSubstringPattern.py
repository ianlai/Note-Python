class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        m = len(s)
        
        sublen = m // 2
        while sublen > 0:
            if m % sublen != 0:
                sublen -= 1
                continue
            #print("sub:", sublen)
            
            n = m // sublen
            matchedSub = 0 
            cur = ""
            for j in range(1, n+1):
                if j == 1:
                    cur = s[:j*sublen]
                    continue
                nxt = s[(j-1)*sublen:j*sublen]
                #print(j, cur, nxt)
                if cur != nxt:
                    break
                matchedSub += 1
            #print("matched:", matchedSub)
            if matchedSub == n - 1:
                return True
        
            sublen -= 1
        return False
        
        