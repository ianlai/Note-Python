class Solution:
    
    # BFS [O(n2), 18%(check board in main), 9%(check board in bfs)]  
    # 1. Find the "O" which can't be flips and set them to "T"
    # 2. Find the "O" which should be flips and flip them to "X"
    # 3. Find the "T" and set them back to "O"
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("BFS")
        if len(board) == 0 or len(board[0]) == 0:
            return 
        
        M, N = len(board), len(board[0])
        
        #self.printBoard(board)
        
        # 1. Find the "O" which can't be flips and set them to "T"
        for i in range(M):
            if board[i][0] == "O":
                self.bfs(board, i, 0, "O", "T")
            if board[i][N-1] == "O":
                self.bfs(board, i, N-1, "O", "T")
                
        for j in range(N):
            if board[0][j] == "O": 
                self.bfs(board, 0, j, "O", "T")
            if board[M-1][j] == "O":
                self.bfs(board, M-1, j, "O", "T")

        #self.printBoard(board)
        
        # 2. Find the "O" which should be flips and flip them to "X"
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    self.bfs(board, i, j, "O", "X")
        
        #self.printBoard(board)
        
        # 3. Find the "T" and set them back to "O"
        for i in range(M):
            for j in range(N):
                if board[i][j] == "T":
                    self.bfs(board, i, j, "T", "O")
                    
        #self.printBoard(board)
    
    def bfs(self, board, i, j, src, dst):
        M, N = len(board), len(board[0])
        
        q = collections.deque([(i, j)])
        while q:
            cur = q.popleft()
            i, j = cur[0], cur[1]
            if i < 0 or i >= M or j < 0 or j >= N:
                continue
            if board[i][j] != src:
                continue
            board[i][j] = dst
            for diff in [(1,0), (-1,0), (0,1), (0,-1)]:
                q.append((i + diff[0], j + diff[1]))
    
    #=====================================================
    
    # DFS [O(n2), 18%(check board in main), 12%(check board in dfs)]  
    # 1. Find the "O" which can't be flips and set them to "T"
    # 2. Find the "O" which should be flips and flip them to "X"
    # 3. Find the "T" and set them back to "O"
    def solve1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print("DFS")
        if len(board) == 0 or len(board[0]) == 0:
            return 
        
        M, N = len(board), len(board[0])
        
        #self.printBoard(board)
        
        # 1. Find the "O" which can't be flips and set them to "T"
        for i in range(M):
            #if board[i][0] == "O":
                self.dfs(board, i, 0, "O", "T")
            #if board[i][N-1] == "O":
                self.dfs(board, i, N-1, "O", "T")
                
        for j in range(N):
            #if board[0][j] == "O": 
                self.dfs(board, 0, j, "O", "T")
            #if board[M-1][j] == "O":
                self.dfs(board, M-1, j, "O", "T")

        #self.printBoard(board)
        
        # 2. Find the "O" which should be flips and flip them to "X"
        for i in range(M):
            for j in range(N):
                #if board[i][j] == "O":
                    self.dfs(board, i, j, "O", "X")
        
        #self.printBoard(board)
        
        # 3. Find the "T" and set them back to "O"
        for i in range(M):
            for j in range(N):
                #if board[i][j] == "T":
                    self.dfs(board, i, j, "T", "O")
                    
        #self.printBoard(board)
    
    def dfs(self, board, i, j, src, dst):
        M, N = len(board), len(board[0])
        if i < 0 or i >= M or j < 0 or j >= N:
            return
        if board[i][j] != src:
            return 
        board[i][j] = dst
        
        self.dfs(board, i+1, j, src, dst)
        self.dfs(board, i-1, j, src, dst)
        self.dfs(board, i, j+1, src, dst)
        self.dfs(board, i, j-1, src, dst)
        
    def printBoard(self, board):
        print()
        for row in board:
            print(row)
        