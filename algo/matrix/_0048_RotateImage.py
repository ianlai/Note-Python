class Solution:
    
    # Traverse matrix circle by circle from inward [O(n2), 80%]
    def rotate(self, matrix: List[List[int]]) -> None:
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
                
        
        
        