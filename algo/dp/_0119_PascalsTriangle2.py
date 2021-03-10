class Solution:
    
    # 1. Brute Force (Top-Down DP without memoization)
    def getRow1(self, rowIndex: int) -> List[int]:
        print("Brute Force")
        
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.helper1(rowIndex, i))
        return ans
        
    def helper1(self, rowIndex, colIndex):
        if colIndex == 0 or colIndex == rowIndex:
            return 1
        return self.helper1(rowIndex-1, colIndex-1) + self.helper1(rowIndex-1, colIndex)
    
    #============================================

    # 2. Top-Down DP (with memoization)
    def getRow2(self, rowIndex: int) -> List[int]:
        print("Top-down DP")
        
        ans = []
        memo = {}
        for i in range(rowIndex + 1):
            ans.append(self.helper2(memo, rowIndex, i))
        return ans
        
    def helper2(self, memo, rowIndex, colIndex):
        if colIndex == 0 or colIndex == rowIndex:
            return 1
        if (rowIndex, colIndex) in memo:
            return memo[(rowIndex, colIndex)]
        result = self.helper2(memo, rowIndex-1, colIndex-1) + self.helper2(memo, rowIndex-1, colIndex)
        memo[(rowIndex, colIndex)] = result
        return result
    
    #============================================
    
    # 3. Bottom-up DP; 2-dimension array, space: O(n^2)
    def getRow3(self, rowIndex: int) -> List[int]:
        print("Buttom-up DP")
        
        row = [[1 for j in range(i+1)] for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j == 0 or j == i: 
                    row[i][j] = 1
                else:
                    row[i][j] = row[i-1][j-1] + row[i-1][j]
        return row[i]

    #============================================
    # 4. Bottom-up DP; 1-dimension array (rolling array), space: O(n)
    def getRow(self, rowIndex: int) -> List[int]:
        print("Buttom-up DP (rolling array)")
        
        row = [[1 for j in range(i+1)] for i in range(2)]
        for i in range(rowIndex+1):
            # add two 0 so that next row will have one more element than the previous row 
            row[i%2].extend([0, 0])
            for j in range(i+1):
                if j == 0 or j == i: 
                    row[i%2][j] = 1
                else:
                    row[i%2][j] = row[i%2-1][j-1] + row[i%2-1][j]
        # remove the last two 0 since we don't need to calculate a new row 
        row[i%2].pop()
        row[i%2].pop()
        return row[i%2]