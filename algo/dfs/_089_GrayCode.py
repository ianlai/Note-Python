from typing import List
import sys
import time
sys.setrecursionlimit(100000)

class Solution:

    # Method1 - Reflect 
    def grayCodeReflect(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        convertArr = [2 ** i for i in range(n)] # 1,2,4,8... 
        cur = [0, 1] #start from 0, 1
        ans = [0, 1]

        #(1) Reflect and then plus convertArr
        #(2) Combine origin array and reflected array
        for i in range(1, n): #2,4,8...
            cur = ans
            reversedArr = [ e + convertArr[i] for e in cur[::-1] ]
            ans = cur + reversedArr 
        return ans

    # Method2 - DFS
    def grayCodeDFS(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        convertArr = [2 ** i for i in range(n)] 
        used = [0] * (2 ** n)
        used[0] = 1
        cur = [0] #start from 0
        ans = []
        isDone = [False]
        self.dfs(convertArr, 2**n, 0, ans, cur, used, 0, isDone)
        # print("Ans: ", ans)
        return ans[0]
    
    #N is 2**n, e.g. N(8) = 2**n(3)
    #isDone will be set to True once the first gray code is found 
    #isDone needs to be list so that it won't be reset in different recursion 
    #cur is one gray code list. 
    #ans can contain all gray code lists but it will cause TLE, so we need to trim it. 
    def dfs(self, convertArr, N, number, ans, cur, used, index, isDone):
        if isDone[0] == True:
            return
        if len(cur) == N:
            #print("Return: ", cur)
            ans.append(cur+[])  #new list 
            isDone[0] = True
            return 
        #print(isDone, number)
        for e in convertArr:
            next_number = number ^ e 
            #print(index, next_number)
            if used[next_number] == 0:
                cur.append(next_number)
                used[next_number] = 1
                self.dfs(convertArr, 
                         N, 
                         next_number, 
                         ans,
                         cur, 
                         used, 
                         index + 1,
                         isDone)
                used[next_number] = 0
                cur.remove(next_number)
s = Solution()


for i in range(15):
    print("=========================")
    print("Gray code: ", i) 
    t1_s = time.process_time_ns()
    ans1 = s.grayCodeReflect(i)
    t1_e = time.process_time_ns()

    t2_s = time.process_time_ns()
    ans2 = s.grayCodeDFS(i)
    t2_e = time.process_time_ns()

    if ans1 == ans2:
        print("Time elapsed - Reflect (ms)", (t1_e - t1_s)/1000000) # CPU seconds elapsed (floating point)
        print("Time elapsed - DFS     (ms)", (t2_e - t2_s)/1000000) # CPU seconds elapsed (floating point)
    else:
        print("[ERROR] The answers are different.")
    print()

    