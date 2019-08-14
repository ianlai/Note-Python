class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None:
            return []
        if digits is "":  #empty string can't use None to capture
            return []
        
        phoneArr = ["",     #1
                    "abc",  #2
                    "def",  #3
                    "ghi",  #4
                    "jkl",  #5
                    "mno",  #6
                    "pqrs", #7
                    "tuv",  #8
                    "wxyz"] #9
        ans = []
        self.dfs(digits, phoneArr, ans, "", 0)
        return ans
    
    def dfs(self, inputStr, phoneArr, ans, cur, index):
        if index == len(inputStr):
            ans.append(cur)
            return 
        for char in phoneArr[int(inputStr[index])-1]:
            self.dfs(inputStr, phoneArr, ans, cur + char, index + 1)
        
        