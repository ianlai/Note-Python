class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        
        start, end = 0, len(s) - 1
        tryRound = 0
        missIdxStart, missIdxEnd = -1, -1
        
        while start < end: 
            if s[start] != s[end]:
                if tryRound == 0:
                    missIdxStart, missIdxEnd = start, end
                    start += 1 
                    tryRound = 1
                elif tryRound == 1:
                    start, end = missIdxStart, missIdxEnd
                    end -= 1
                    tryRound = 2
                else: 
                    return False
            else:
                start += 1 
                end -= 1
        return True