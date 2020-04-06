class Solution:
    
    # Memoization (DP): 74%
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, 0, p, 0, {})
    
    def helper(self, s, si, p, pi, memo):
        if (si, pi) in memo:
            return memo[(si, pi)]
        
        # string ends 
        if si == len(s):
            #pattern
            # a***: True
            # aaa : False
            # **  : True
            # a   : False
            # a*a : False
            # *a  : False 
            # aaa*: False
            # a*a*: True
            removeOne = False
            for i in range(len(p)-1, pi-1, -1):
                if p[i] == "*":
                    removeOne = True
                else:
                    if removeOne:
                        removeOne = False
                    else:
                        memo[(si, pi)] = False
                        return False
            return True
        
        # pattern ends 
        if pi == len(p):
            memo[(si, pi)] = False
            return False
        
        # recursive of 3 cases: "*", ".", letter
        # if "*", split to match many and no match
        #   match zero: pattern proceeds by one 
        #   match many: check the previous char -> if "." or same char, then pass; otherwise, false
        # if ".", check the next char is "*" or not
        #   if yes, patterns go next and let "*" case handle
        #   if no, just pass one char for both s and p
        # if letter, check the next char is "*" or not
        #   if yes, patterns go next and let "*" case handle
        #   if no, compare the letters are the same or not -> if no, false; if true, proceeds
        if p[pi] == "*":
            pre = p[pi-1] 
            matchMany = False
            if pre == s[si] or pre == ".":
                matchMany = self.helper(s, si+1, p, pi, memo)
            matchZero = self.helper(s, si, p, pi+1, memo)
            memo[(si, pi)] = matchZero or matchMany
            return memo[(si, pi)]
        elif p[pi] == ".":
            if pi == len(p)-1:  #last char
                memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo)
            elif pi < len(p)-1 and p[pi+1] != "*":
                memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo)
            elif pi < len(p)-1 and p[pi+1] == "*": 
                memo[(si, pi)] = self.helper(s, si, p, pi+1, memo)
            return memo[(si, pi)]
        else: 
            if pi == len(p)-1:  #last char
                if p[pi] != s[si]:
                    memo[(si, pi)] = False
                    return False
                memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo)
                return memo[(si, pi)]
            elif pi < len(p)-1 and p[pi+1] != "*":
                if p[pi] != s[si]:
                    memo[(si, pi)] = False
                    return False
                memo[(si, pi)] = self.helper(s, si+1, p, pi+1, memo) 
                return memo[(si, pi)]
            elif pi < len(p)-1 and p[pi+1] == "*": 
                memo[(si, pi)] = self.helper(s, si, p, pi+1, memo)
                return memo[(si, pi)]
                
                