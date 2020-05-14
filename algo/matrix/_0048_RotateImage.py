class Solution:
    # Transpose than reverse [time: O(n2), 93% ; space: O(1)]
    def rotate(self, matrix: List[List[int]]) -> None:
        def printMatrix(matrix):
            for i in range(len(matrix)):
                print(i, matrix[i])
            print()
            
        n = len(matrix)
        
        #printMatrix(matrix)
        
        #Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #printMatrix(matrix)
        
        #Revese the columns
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
        #printMatrix(matrix)
        
        
    # ================================================= 
    
    # Traverse matrix circle by circle from inward [time: O(n2), 80% ; space: O(n2) for the coordinate array]
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # return an array of coordinates to traverse the circle clockwise
        def transform(start, n): 
            if n == 1:
                return [start]
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            res = []
            total = 4 * (n - 1)
            cur = start
            for i in range(total):
                res.append(cur[:])
                d = directions[(i)//(n-1)]
                cur[0], cur[1] = cur[0] + d[0], cur[1] + d[1]
                #print(i, d, res)
            return res 

        n = len(matrix)
        outloopRound = n // 2
        
        for i in range(outloopRound):
            total = 4 * (n - 1)
            arr = transform([i, i], n)
            # print("==========" , i, "==========")
            # print("n    :", n)
            # print("total:", total)
            #print(arr)
            
            temp = collections.deque([]) 
            count = 0 

            for j in range(len(arr) + n-1):
                j %= total
                #print("j: ", j)
                x, y = arr[j][0], arr[j][1]
                if count < n-1:
                    temp.append(matrix[x][y])
                else:
                    try:
                        temp.append(matrix[x][y])
                        matrix[x][y] = temp.popleft()
                    except:
                        print(x, y)
                        raise
                count += 1
                # print(temp)
                # for i in range(len(matrix)):
                #     print(i, matrix[i])
                # print()
            n -= 2
                
        
        
        