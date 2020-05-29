class Solution(object):
    
    # Two-layer loops [74%]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        result = ""
        for center in range(len(s)):
            sub = self.findLongestPalindrome(s, center, center)
            if len(sub) > len(result):
                result = sub 
            sub = self.findLongestPalindrome(s, center, center+1)
            if len(sub) > len(result):
                result = sub 
        return result
    
    def findLongestPalindrome(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left  -= 1
            right += 1
        return s[left+1:right]
        