class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [["Q"]]
        cur    = []
        numAns = []
        strAns = []

        self.bfs(n, numAns, cur, 0)
        if len(numAns) == 0: 
            return []
        #print(numAns)

        self.buildString(numAns, strAns)
        #print(strAns)
        return strAns
    
    def bfs(self, n, ans, cur, row):
        if row == n:
            # print(">> ans: ", cur)
            ans.append(cur)
            return 
        for i in range(n):
            if self.valid(cur, i):
                # print("valid: o ", cur, i)
                self.bfs(n, ans, cur+[i], row+1)
            else:
                # print("valid: x ", cur, i)
                continue
                
    def valid(self, cur, col):
        n = len(cur)
        #print(cur, col)
        for i in range(len(cur)):
            #print(col+(n), cur[i]+i)
            #print(abs(col-(n)), abs(cur[i]-i))
            if col == cur[i]:       #same col 
                return False
            if col + n == cur[i] + i: #same left diagonal
                return False
            if col - n == cur[i] - i: #same right diagonal
                return False
        return True
    
    def buildString(self, numsArr, strArr):
        m = len(numsArr)
        n = len(numsArr[0])
        for i in range(m):
            cur = []
            for e in numsArr[i]:
                s = ["."] * n
                s[e] = "Q"
                string = "".join(s)
                cur.append(string)
            strArr.append(cur)
            