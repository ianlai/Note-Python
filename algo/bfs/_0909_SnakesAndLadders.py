class Solution:
    
    # BFS  
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if len(board) == 0 or len(board[0]) == 0:
            return -1
        n = len(board)
        
        ####### DEBUG #######
        # sampleBoard = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         num = i * n + j + 1
        #         coo = self.numToCoordinate(board, num)
        #         sampleBoard[coo[0]][coo[1]] = num
        # for i, row in enumerate(sampleBoard):
        #     print(i, row) 
        # for i, row in enumerate(board):
        #     print(i, row)
            
            
        start = (n - 1, 0)
        deque = collections.deque([(1, start)])  #num, coordinate
        visited = set()
        count = 0 
        while deque:
            for step in range(len(deque)): 
                curNum, curCoo = deque.popleft()
                #print(curNum, curCoo)
                if curNum == n * n:
                    return count
                
                for i in range(1, 7):
                    nextNum = curNum + i
                    if nextNum > n * n:
                        break
                    
                    nextCoo = self.numToCoordinate(board, nextNum)  #normal 
                    
                    if board[nextCoo[0]][nextCoo[1]] != -1 : #snake or ladder
                        nextNum = board[nextCoo[0]][nextCoo[1]]
                        nextCoo = self.numToCoordinate(board, nextNum)
        
                    if nextNum in visited:
                        continue
        
                    deque.append((nextNum, nextCoo))
                    visited.add(nextNum)
            count += 1
            #print("------", count, "------")
        return -1 #can't arrive
            
    def numToCoordinate(self, board, num):
        n = len(board)
        num -= 1
        row = n - 1 - num // n 
        if (n - 1 - row) % 2 == 0:  #go right
            col = num % n 
        else: #go left
            col = n - 1 - (num % n) 
        return row, col 