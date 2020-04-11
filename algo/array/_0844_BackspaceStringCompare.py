class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sarr = []
        tarr = []
        
        for s in S:
            if s == '#' and len(sarr) >= 1:
                sarr.pop()
            if s != '#':
                sarr.append(s)
        
        for t in T:
            if t == '#' and len(tarr) >= 1:
                tarr.pop()
            if t != '#':
                tarr.append(t)
                
        return sarr == tarr