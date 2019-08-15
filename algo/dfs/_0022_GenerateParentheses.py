class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(ans, "", n, 0)
        return ans
    
    # L: how many "(" can be used now
    # R: how many ")" can be used now
    def dfs(self, ans, cur, L, R):
        if L==0 and R==0:
            ans.append(cur)
            return 
        if L > 0:
            self.dfs(ans, cur + '(', L-1, R+1)
        if R > 0:
            self.dfs(ans, cur + ')', L, R-1)
        return 