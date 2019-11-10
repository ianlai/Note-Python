class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0 :
            return 0
        
        maxCount = 0 
        for i in range(len(s)):
            charMap = {}
            
            for j in range(i, len(s)):
                cur = s[j]
                if cur not in charMap:
                    charMap[cur] = 1
                    maxCount = max(maxCount, len(charMap))
                else:
                    maxCount = max(maxCount, len(charMap))
                    break
                    
        return maxCount