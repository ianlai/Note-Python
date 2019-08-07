class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #pas = [[0] * numRows] * numRows
        #pas = [[0 for j in range(n)] for i in range(m)]
        #pas = [[0 for j in range(i)] for i in range(m)]
        #m = n = numRows

        pas = [[0 for j in range(i+1)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:   #j==0 is leftmost 1, j==i is rightmost 1
                    pas[i][j] = 1
                else:
                    pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
        return pas
        