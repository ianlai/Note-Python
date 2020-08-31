class Solution:
    
    #Calculate the cummulative matrix first, then reduce the redundant parts for each point [O(n), 94%]
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j-1] 
                
        for j in range(n):
            for i in range(1, m):
                mat[i][j] += mat[i-1][j]
        

        res = [[0 for j in range(n)] for i in range(m)]
        #self.debugPrint(mat)
        
        for i in range(m):
            minRow, maxRow = max(0, i-K), min(m-1, i+K)
            for j in range(n):
                minCol, maxCol = max(0, j-K), min(n-1, j+K)
                res[i][j] = mat[maxRow][maxCol]
                if minCol - 1 >= 0:
                    res[i][j] -= mat[maxRow][minCol-1]
                if minRow - 1 >= 0:
                    res[i][j] -= mat[minRow-1][maxCol]
                if minCol - 1 >= 0 and minRow - 1 >= 0:
                    res[i][j] += mat[minRow-1][minCol-1]
        #self.debugPrint(res)
        return res
        
        
    def debugPrint(self, mat):
        m, n = len(mat), len(mat[0])
        #print 
        for i in range(m):
            for j in range(n):
                print(mat[i][j], " ", end = "")
            print()
        print("------------")