class Solution:
    
    # Memoization search (DP): 40% 
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, 0, p, 0, {})
    
    def helper(self, s, si, p, pi, memo):
        # Memoization 
        if (si, pi) in memo:
            return memo[(si, pi)] 
        
        # End condition (when string or pattern ends)
        if si == len(s): #string ends
            # if patterns only left "*", then true; otherwise, false
            for i in range(pi, len(p)):
                if p[i] != "*":
                    memo[(si, pi)] = False
                    return False
            memo[(si, pi)] = True
            return True
            
        if pi == len(p): #pattern ends 
            memo[(si, pi)] = False
            return False
        
        # Recursive of the 3 cases
        if p[pi] == "*":
            matchZero = self.helper(s, si, p, pi+1, memo)
            matchSome = self.helper(s, si+1, p, pi, memo) 
            memo[(si, pi)] = matchZero or matchSome
            return memo[(si, pi)]
            
        elif p[pi] == "?":
            memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo)
            return memo[(si, pi)]
            
        else:
            if p[pi] != s[si]:
                memo[(si, pi)] = False
                return False
            memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo)
            return memo[(si, pi)]
        
        
            
    