class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s is None or len(s) == 0:
            return None
        ans = []
        self.dfs(s, [], ans)
        return ans
    
    def dfs(self, s, cur, ans):
        #print(s, cur, ans)
        if len(s) == 0:
            ans.append(cur)  
        for i in range(1, len(s)+1):
            #print("  ", i, s[:i])
            if self.isPal(s[:i]):
                #print("  remaining ", s[i:])
                self.dfs(s[i:], cur + [s[:i]] , ans)
                
    def isPal(self, string):
        if string == string[::-1]:
            return True
        return False
