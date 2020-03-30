class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 :
            return []
        
        m, n = len(matrix), len(matrix[0])
        size = m * n
        bu, bd, bl, br = 0, m-1, 0, n-1 
        d = 1  #1: right, 2: down, 3: left, 4: up  
        i, j = 0, -1
        ans = []

        while len(ans) < size:
            if d == 1:
                if j == br:
                    d = 2
                    bu += 1
                    continue
                else:
                    j += 1
            elif d == 2:
                if i == bd:
                    d = 3
                    br -= 1
                    continue
                else:
                    i += 1
            elif d == 3:
                if j == bl:
                    d = 4
                    bd -= 1
                    continue
                else:
                    j -= 1
            elif d == 4:
                if i == bu:
                    d = 1
                    bl += 1
                    continue
                else:
                    i -= 1
            ans.append(matrix[i][j]) 
        #print(ans)
        return ans
            
            