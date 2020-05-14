class Solution:
    
    # Bottom-up DP: [O(n2), 23%]
    # 0. basic idea is, A[i:j] could be palindrome only when 
    #    (1) A[i+1:j-1] is also a palindrome
    #    (2) s[i] == s[j]
    # 1. each cell stores the boolean whether it's a palindrome 
    # 2. i, j, diff should be 2 layer loops, instead of 3 layer loops
    def countSubstrings(self, s: str) -> int:    
        if len(s) <= 1:
            return len(s)
        
        n = len(s)
        dp = [[1 for j in range(n)] for i in range(n)] 
        
        ### count diff=0 (diagonal)
        ans = n 

        ### count diff > 1
        for diff in range(1, n):
            #for i in range(len(s)):
            #    print(i, dp[i])
            #print("---------------")
            
            for i in range(0, n-diff):
                j = i + diff  #use 2 loops of diff and i, instead of i and j 
                #print(diff, "(", i, j, ")")
                dp[i][j] = int(dp[i+1][j-1] and s[i] == s[j])    
                if dp[i][j] == 1:
                    ans += 1
        return ans
    
    # =========================================================================

    
    # Bottom-up DP  [TLE: can't solve the special case with many continuous repeative elements]
    # 1. each cell stores the boolean whether it's a palindrome 
    # 2. i, j, diff use 3 layer loops
    def countSubstrings1(self, s: str) -> int:    
        if len(s) <= 1:
            return len(s)
        
        dp = [[True for j in range(len(s))] for i in range(len(s))] 
        
        ans = len(s) #diagonal
        diff = 1 
        while diff <= len(s) - 1:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if j - i == diff:
                        dp[i][j] = dp[i+1][j-1] and s[i] == s[j]      
                        if dp[i][j] == True:
                            ans += 1
            # for i in range(len(s)):
            #     print(i, dp[i])
            # print("---------------")
            diff += 1
            
        # ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] == True:
                    ans += 1
            
        return ans
    
    # =========================================================================
    
    # Bottom-up DP [TLE: can't solve the special case with many continuous repeative elements]
    # 1. each cell stores the number of palindroms (complex and incorrect for the repeating count)
    # 2. i, j, diff use 3 layer loops (slow)
    def countSubstrings1(self, s: str) -> int:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return 0
                l += 1
                r -= 1
            return 1
    
        if len(s) <= 1:
            return len(s)
        
        dp = [[1 for j in range(len(s))] for i in range(len(s))] 
        
        diff = 1 
        while diff <= len(s) - 1:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if j - i == diff:
                        dp[i][j] = dp[i][j-1] + dp[i+1][j] + isPalindrome(s, i, j)
                        dp[i+1][j] = 0 
                        
            # for i in range(len(s)):
            #     print(i, dp[i])
            # print("---------------")
            diff += 1
            
        return dp[0][len(s)-1]
        
    # =========================================================================
    
    # Top-down DP [TLE: can't solve the special case with many continuous repeative elements]
    # 1. store number of palindrome in memo[i:j]
    # 2. judge the palindrome by O(n) function (too slow)
    def countSubstrings2(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        return self.helper(s, 0, len(s)-1, {})
    
    def helper(self, s, l, r, memo):
        if l > r:
            return 0
        if (l, r) in memo:
            return 0  # memo[(l, r)]
        
        ###### Handle coninuous repeatition #####
        length = r - l + 1
        sameNum = 0
        for i in range(l+1, r+1):
            if s[l] != s[i]:
                break
            else:
                sameNum += 1
                
        if length > 1 and sameNum + 1 == length:
            wholePart = (length + 1) * length // 2
            memo[(l,r)] = wholePart
            print("special:", l, r,"->", wholePart)
            
            for i in range(l, r+1):
                for j in range(i, r+1):
                    memo[(i, j)] = 1
                    
            return wholePart
        ###### Handle coninuous repeatition #####
                
                
        leftPart = self.helper(s, l, r-1, memo)
        rightPart = self.helper(s, l+1, r, memo)
        wholePart = leftPart + rightPart
        if self.isPalindrome(s, l, r):
            wholePart += 1
        print(l, r, wholePart)
        memo[(l,r)] = wholePart
        return wholePart
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
        