class Solution:
    
    # Top-down DP 
    # time = O(N*L*L) if no memo
    # time = min(2^NL, 26^L) number of substrings in words if memo  [5%]
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        #words.sort()
        ans = 0
        memo = {}
        for word in words:
            #print("===== word: ", word, "=====")
            ans = max(ans, self.helper(words, word, memo))
        return ans
    
    def helper(self, words, word, memo):
        if len(word) == 0 or word not in words:
            return 0
        if word in memo:
            return memo[word]
        
        maxValue = 1
        for i in range(len(word)):
            nextWord = word[:i] + word[i+1:]
            if nextWord in words:
                maxValue = max(maxValue, 1 + self.helper(words, nextWord, memo))
        memo[word] = maxValue
        return maxValue