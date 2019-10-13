class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None or len(s) == 0:
            return -1
        
        map = {}
        
        # Traverse 1 
        for char in s:
            map[char] = map.get(char, 0) + 1
            
        # Traverse 2 
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i 
        
        return -1 