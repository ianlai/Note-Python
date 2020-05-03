class Solution:
    
    # Bottom-up DP: [O(M*N), 49%] 
    #
    # DP[i][j] means len of common prefix starting from A[i] and B[j]
    # A = [5,2,3,2,1,9]
    # B = [3,2,1,4]
    # DP = 
    # 0 [0, 0, 0, 0, 0]
    # 1 [0, 1, 0, 0, 0]
    # 2 [3, 0, 0, 0, 0]
    # 3 [0, 2, 0, 0, 0]
    # 4 [0, 0, 1, 0, 0]
    # 5 [0, 0, 0, 0, 0]
    # 6 [0, 0, 0, 0, 0]
    
    def findLength(self, A: List[int], B: List[int]) -> int: 
        
        if not A and not B:
            return 0
        
        # m = len(A) + 1 
        # n = len(B) + 1  
        # make the matrix one extra column and row so that we don't need to handle the edge cases
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]  
        ans = 0
        for i in range(len(A)-1, -1, -1):  #loop for len(A)-1 (not from extra space)
            for j in range(len(B)-1, -1, -1):  #loop for len(B)-1 (not from extra space)
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans, dp[i][j])
        #print out
        # for i in range(len(A)+1):
        #     print(i, dp[i])
            
        return ans
    
    #Brute force: loop len of char, loop A 
    def findLength1(self, A: List[int], B: List[int]) -> int:      
        #Todo: isSubarray()
        
        maxLen = 0
        for n in range(1, len(A)):
            for i in range(0, len(A) - n + 1):
                cur = A[i:i+n]
                print
                #if cur in B:
                if isSubarray(cur, B):
                    print(cur)
                    maxLen = max(maxLen, len(cur))
        return maxLen