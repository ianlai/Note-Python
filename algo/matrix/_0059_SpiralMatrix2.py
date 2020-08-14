class Solution:
    
    #4 directions, 4 borders [O(mn), 75%]
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        res = [ [-1 for j in range(n)] for i in range(n) ]
        
        #directions = ["r", "d", "l", "u"]
        d = "r"
        bu, bd = 0, n-1
        bl, br = 0, n-1
        total = n * n 
        i, j = 0, -1 
        
        for count in range(total):
            if d == "r":
                if j == br:
                    d = "d"
                    bu += 1
                    i += 1
                else:
                    j += 1
                    
            elif d == "d":
                if i == bd:
                    d = "l"
                    br -= 1
                    j -= 1
                else:
                    i += 1
            
            elif d == "l":
                if j == bl:
                    d = "u"
                    bd -= 1
                    i -= 1
                else:
                    j -= 1
                
            elif d == "u":
                if i == bu:
                    d = "r"
                    bl += 1
                    j += 1
                else:
                    i -= 1
            #print(count, ":", i, "-", j)
            res[i][j] = count + 1
        return res
        
        
        