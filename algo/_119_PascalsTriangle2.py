class Solution:
    # 2-dimension array, space: O(n^2)
    def getRowSpaceNN(self, rowIndex: int) -> List[int]:
        row = [[1 for j in range(i+1)] for i in range(rowIndex+1)]
        if rowIndex == 0:
            return row[0]
        if rowIndex == 1:
            return row[1]
        for i in range(2, rowIndex+1):
            for j in range(i+1):
                if j == 0:
                    row[i][j] = 1
                elif j == i:
                    row[i][j] = 1
                else:
                    row[i][j] = row[i-1][j-1] + row[i-1][j]
        #print(row)
        return row[i]

    # rolling array, space: O(n)
    def getRow(self, rowIndex: int) -> List[int]:
        row = [[1 for j in range(i+1)] for i in range(2)]
        if rowIndex == 0:
            return row[0]
        if rowIndex == 1:
            return row[1]
        for i in range(2, rowIndex+1):
            # create 2 spaces for the next row 
            row[i%2].append(0)  
            row[i%2].append(0)
            for j in range(i+1):
                if j == 0:
                    row[i%2][j] = 1
                elif j == i:
                    row[i%2][j] = 1
                else:
                    row[i%2][j] = row[i%2-1][j-1] + row[i%2-1][j]
            #print(row[0])
            #print(row[1])
        return row[i%2]
                
        
        