from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None:
            return None
        self.board = board
        self.dfs()
    
    def dfs(self):
        row, col = self.findNext()
        if row == -1 and col == -1:
            return True 
        
        for num in range(1, 10):
            if self.isValid(row, col, num):
                self.board[row][col] = str(num)
                if self.dfs():
                    return True
                self.board[row][col] = '.'
        return False

                
    def findNext(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1
    
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True

    def isValid(self, row, col, num):
        boxrow = row - row%3
        boxcol = col - col%3

        for i in range(9):
            if self.board[i][col] == str(num):
                return False   #same col
            
        for j in range(9):
            if self.board[row][j] == str(num):
                return False   #same row
        
        if not self.checksquare(boxrow, boxcol, str(num)):
            return False       #same square
        
        return True

def printBoard(board):
    for row in board:
        print(row)
        
s = Solution()
testInput =      [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
expectedOutput = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

print("Input:")
printBoard(testInput)

s.solveSudoku(testInput)

print("Output:")
printBoard(testInput)

print("Expected output:")
printBoard(expectedOutput)

print("Answer: ", testInput == expectedOutput)