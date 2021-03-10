class Solution:

    #2021.03.11
    def generate(self, numRows: int) -> List[List[int]]:
        
        #initialization
        pas = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(0)
            pas.append(row)
        
        #traverse and set the values
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    pas[i][j] = 1
                else:
                    pas[i][j] = pas[i-1][j-1] + pas[i-1][j]  
                    
        return pas
    
    #2019.08.16
    def generate1(self, numRows: int) -> List[List[int]]:
        pas = [[0 for j in range(i+1)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:   #j==0 is leftmost 1, j==i is rightmost 1
                    pas[i][j] = 1
                else:
                    pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
        return pas