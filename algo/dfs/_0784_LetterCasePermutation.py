class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S is None: 
            return []
        if S == "":
            return []
        ans = []
        self.dfs(S, ans, "", 0)
        return ans
    
    def dfs(self, S, ans, cur, index):
        if index == len(S):
            ans.append(cur+"")
            return
        if S[index].isdigit():
            #print(S[index], "digit")
            self.dfs(S, ans, cur + S[index], index+1)
        if S[index].isalpha():
            #print(S[index], "alpha")
            self.dfs(S, ans, cur + S[index].lower(), index+1)    
            self.dfs(S, ans, cur + S[index].upper(), index+1)
        return