class Solution:
    
    # DP [79%]
    def knightDialer(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 10
        dp = [[1 for j in range(N)] for i in range(10)]
        for j in range(1, N):
            dp[1][j] = dp[6][j-1] + dp[8][j-1]
            dp[2][j] = dp[7][j-1] + dp[9][j-1]
            dp[3][j] = dp[4][j-1] + dp[8][j-1]
            dp[4][j] = dp[3][j-1] + dp[9][j-1] + dp[0][j-1]
            dp[5][j] = 0
            dp[6][j] = dp[1][j-1] + dp[7][j-1] + dp[0][j-1]
            dp[7][j] = dp[2][j-1] + dp[6][j-1]
            dp[8][j] = dp[1][j-1] + dp[3][j-1]
            dp[9][j] = dp[2][j-1] + dp[4][j-1]
            dp[0][j] = dp[4][j-1] + dp[6][j-1]
        #print(dp)
        count = 0
        for i in range(10):
            count += dp[i][N-1]
        return count % (10 ** 9 + 7)
            
    # BFS [TLE]
    def knightDialer1(self, N: int) -> int:
        if N == 0 : return 0
        if N == 1 : return 10
        mp = {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
            0: [4,6]
        }
        queue = deque([1,2,3,4,5,6,7,8,9,0])
        count = 0
        for i in range(N):
            for _ in range(len(queue)):
                if i == N-1: #last run 
                    #print(queue)
                    count = len(queue)
                    break 
                cur = queue.popleft()
                for nxt in mp[cur]:
                    queue.append(nxt)
        return count % (10 ** 9 + 7)