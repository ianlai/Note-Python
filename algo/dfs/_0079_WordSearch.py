
# Solution: 
# (1) Not using visited matrix, update the original matrix directly
# (2) Not using index of word, passing the slice without head 
# (3) Do the validation check in the function, not in for loop (before function)
#
# But I think using visited instead of updating the original matrix is clear. 
# So I keep use this approach. 

class Solution:

    # Backtracking, better coding style (70%, O(m*n*4^L))
    # >> Only reset one element in visited for each step in 2-layer loop
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, visited, i, j, wordIdx):  #inner function needs to go before calling 
            #print("b:", board[i][j], " | w:", word[wordIdx], " | wordIdx:", wordIdx)
            if board[i][j] != word[wordIdx]:
                return False
            if wordIdx+1 == len(word):
                return True
            for d0, d1 in dirList:
                #print(">>", d)
                next_i, next_j = i + d0, j + d1
                if not (0 <= next_i < len(board) and 0 <= next_j < len(board[0])):
                    continue
                if visited[next_i][next_j] == 1:
                    continue
                visited[next_i][next_j] = 1
                if dfs(board, word, visited, next_i, next_j, wordIdx+1):
                    return True
                visited[next_i][next_j] = 0
            return False
        
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        
        rows = len(board)
        cols = len(board[0])
        dirList = [(1,0), (0,1), (-1,0), (0,-1)]  #variable can be used by inner function 
        visited = [[0 for _ in range(cols)] for j in range(rows)]
        
        # Main 2-layer loop: traverse all the elements and run dfs on it 
        for i in range(rows):
            for j in range(cols):
                #print("Start: ", board[i][j])
                visited[i][j] = 1
                if dfs(board, word, visited, i, j, 0):
                   return True
                visited[i][j] = 0
        return False
    
    #==========================================================
    
    # Backtracking (5%, O(m*n*4^L))
    # >> Reset the visited matrix for each step in 2-layer loop
    def exist2(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, dirList, visited, i, j, wordIdx):
            #print("b:", board[i][j], " | w:", word[wordIdx], " | wordIdx:", wordIdx)
            if board[i][j] != word[wordIdx]:
                return False
            if wordIdx+1 == len(word):
                return True
            visited[i][j] = 1 
            for d in dirList:
                #print(">>", d)
                next_i, next_j = i+d[0], j+d[1]
                if not (0 <= next_i < len(board) and 0 <= next_j < len(board[0])):
                    continue
                if visited[next_i][next_j] == 1:
                    continue
                visited[next_i][next_j] = 1
                ans = dfs(board, word, dirList, visited, next_i, next_j, wordIdx+1)
                visited[next_i][next_j] = 0
                if ans:
                    return True
            return False
        if len(word) == 0:
            return True
        if len(board) == 0:
            return False
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        dirList = [(1,0), (0,1), (-1,0), (0,-1)]
        visitedConst = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        ans = False
        for i in range(self.ROWS):
            for j in range(self.COLS):
                #print("Start: ", board[i][j])
                visited = [m[:] for m in visitedConst]
                #print(visited)                                         
                if dfs(board, word, dirList, visited, i, j, 0):
                   return True
        return False