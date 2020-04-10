class Solution:
    
    # Brute force / DFS: O(n^3)
    #   0 2
    #   0 3 
    #   0 len(s) - 1
    #   1 3
    #   1 4
    # 1 len(s) - 1 
    # ...
    
    # Two loops:   O(n2)
    
    # Two pointers: O(n)
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        p1, p2 = 0, 0
        ans = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        
        while p2 < len(s):
            count[s[p2]] = count[s[p2]] + 1 
            while p1 < len(s) and count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s[p2:])
                count[s[p1]] = count[s[p1]] - 1 
                p1 += 1
            p2 += 1 
        return ans 