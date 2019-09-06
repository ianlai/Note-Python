class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s is None or len(s) == 0:
            return True
        if t is None or len(t) == 0:
            return False
        
        sp, tp = 0, 0
        while True:
            if s[sp] == t[tp]: 
                sp += 1
                tp += 1
            else:
                tp += 1
            if sp == len(s):
                return True
            if tp == len(t):
                return False