 class Solution:
    def titleToNumber(self, s: str) -> int:
        
        ans = 0
        digit = 0
        for i in range(len(s)-1, -1, -1):
            ans += (ord(s[i]) - 64) * 26 ** digit
            digit += 1
        return ans
        