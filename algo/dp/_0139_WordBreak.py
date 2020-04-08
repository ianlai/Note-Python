class Solution:
    
    # Backtracking with slice approach (TLE)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordDict):
            if len(s) == 0:
                return True
            if len(wordDict) == 0:
                return False

            for i in range(0, len(s)):
                substr = s[:i+1]
                if substr in wordDict:
                    if helper(s[len(substr):], wordDict):
                        return True
            return False
        return helper(s, wordDict)
    

    # Memoization with index approach (30%)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordDict, startIdx, memo):
            if len(s) == startIdx:
                return True
            if len(wordDict) == 0:
                return False
            if startIdx in memo:
                return memo[startIdx]
            
            for j in range(startIdx, len(s)):  #be careful of the indice
                substr = s[startIdx:j+1]       #be careful of the indice
                if substr in wordDict:
                    if helper(s, wordDict, j+1, memo):  #be careful of the indice
                        memo[startIdx] = True
                        return True
            memo[startIdx] = False
            return False
        return helper(s, wordDict, 0, {})
    
    # DP .....