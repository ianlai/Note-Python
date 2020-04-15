class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        def checkRow(board):
            for i in range(m):
                s = set([])
                for j in range(n):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True
        
        def checkCol(board):
            for j in range(n):
                s = set([])
                for i in range(m):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True
        
        def checkBlock(board):
            for outer in range(9):
                x, y = outer % 3, outer // 3
                s = set([])
                for inner in range(9):
                    u, v = inner % 3, inner // 3
                    i = x * 3 + u
                    j = y * 3 + v
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True
                
        return checkRow(board) and checkCol(board) and checkBlock(board)
    
        