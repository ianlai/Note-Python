class Solution:
    
    # Iterative DP: [O(n2), 83%]
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def printMat(mat):
            for i in range(len(mat)):
                print([str(x) for x in mat[i]])
            print()
            
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        size = 0 
        
        #initialize 
        dp[0][0] = int(matrix[0][0])
        size = max(size, dp[0][0])
        
        for i in range(1, m):
            # dp[i][0] = max(dp[i-1][0], int(matrix[i][0]))  #wrong definition 
            dp[i][0] = int(matrix[i][0])
            size = max(size, dp[i][0])
        for j in range(1, n):
            # dp[0][j] = max(dp[0][j-1], int(matrix[0][j]))
            dp[0][j] = int(matrix[0][j])
            size = max(size, dp[0][j])
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
                size = max(size, dp[i][j])
        #printMat(matrix)
        #printMat(dp)
        # return dp[m-1][n-1] ** 2   #wrong definition 
        return size ** 2
        
    
    
    # Brute Force: [O(n4), 5%]
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        size = 0
        for i in range(m):
            for j in range(n):
                max_len = min(i, j) + 1 
                for l in range(max_len):
                    if self.isSquare(matrix, i, j, l):
                        size = max(size, (l+1)*(l+1))
        return size
    def isSquare(self, matrix, m, n, l):
        if l == 0:
            if matrix[m][n] == "1": return True
            else: return False
        x = m - l
        y = n - l
        for i in range(x, x+l+1):
            for j in range(y, y+l+1):
                if matrix[i][j] == "0":
                    return False
        return True