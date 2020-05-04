class Solution:
    
    #  A: [2,1,4,7,3,2,5]
    # dp: [0,0,0,0,4,5,0]  //the mountain len which ends at the current point
    # Actually, we just calculate the dp by it's own condition, not a real DP 
    # Traverse and decide the status: [42%, O(n)]
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        lastMinIdx = 0
        dp = [0] * len(A)
        goup = False 
        lenFromLastMin = 0
        
        for i in range(2, len(A)):
            if A[i-2] < A[i-1] < A[i]:   #go up 
                goup = True
                dp[i] = 0 
            elif A[i-2] > A[i-1] > A[i]: #go down 
                if goup == True:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = 0
            elif A[i-2] < A[i-1] > A[i]: #top
                goup = True
                dp[i] = i - lastMinIdx + 1 
            elif A[i-2] >= A[i-1] < A[i]: #valley
                lastMinIdx = i-1
                goup = True
                dp[i] = 0    
        #print(dp)
        return max(dp)