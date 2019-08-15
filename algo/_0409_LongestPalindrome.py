class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        # initialize
        char_set = set()
        longest_count = 0
        for char in s:
            if char not in char_set: 
                char_set.add(char)
            else:
                char_set.remove(char)
                longest_count += 2
                
        #put a single char into the center of pairs 
        if len(char_set) > 0:
            longest_count +=1 
            
        return longest_count             
            