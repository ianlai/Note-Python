class Solution:
    
    ### Approch-1: Form the permutation string digit by digit 
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0 or k == 0:
            return ""
        
        permutationStr = ""
        remainingArr = list(range(1, n+1)) #1,2,3,...,n
            
        while n > 0:
            print("----------------")
            print("n=", n, "k=", k)
            numOfGroup = n 
            numInGroup = math.factorial(n-1)
            seqOfGroup, seqInGroup = divmod(k-1, numInGroup) #return indices 

            #print(numOfGroup, numInGroup, " | ", seqOfGroup, seqInGroup) 
            #print(remainingArr)
            
            permutationStr += str(remainingArr[seqOfGroup])
            remainingArr.remove(remainingArr[seqOfGroup])

            # next digit
            k = seqInGroup + 1
            n -= 1
        
        print("permutationStr:", permutationStr)
        return permutationStr
    
    
    ### Approch-2: DFS - only create permutation sequence at k (TLE) 
    def getPermutation1(self, n: int, k: int) -> str:
        if n == 0 or k == 0:
            return ""
        if n == 1:
            return "1"
        base = "123456789"
        used = [0] * n 
        counter = [0, 0]
        self.dfs1(base[:n], k, [], used, counter)
        
        #print(counter[0], counter[1])
        return ''.join(counter[1])
    
    def dfs1(self, base, k, cur, used, counter):
        #print(base, "k=", k , " / ", cur, " / ",counter)
        
        if len(cur) == len(base):
            #ans.append(cur)
            counter[0] += 1
            counter[1] = cur
            #print(">> counter[0]++ >> No = ", counter[0], counter[1])
            # if counter[0] == k:  #kth ans
            #     counter[1] = cur
            return 
        
        if counter[0] == k:  #kth ans
            return
        
        for i in range(len(base)):
            if used[i] == 0:
                used[i] = 1
                self.dfs1(base, k, cur + [base[i]], used, counter)
                used[i] = 0
    
    
    ### Approch-3: DFS - create all permutation sequence (TLE) 
    def getPermutation2(self, n: int, k: int) -> str:
        if n == 0 or k == 0:
            return ""
        if n == 1:
            return "1"
        base = "123456789"
        used = [0] * n 
        ans = []
        self.dfs2(base[:n], k, [], ans, used)
        #print("Final ans:", ans)
        ansk = "".join(ans[k-1])
        return ansk
    
    def dfs2(self, base, k, cur, ans, used):
        #print(base, ans, cur, "k=", k )
        if len(ans) == k:
            return 
        
        if len(cur) == len(base):
            #print("ans append")
            ans.append(cur)
            return 
            
        for i in range(len(base)):
            if used[i] == 0:
                used[i] = 1
                self.dfs2(base, k, cur + [base[i]], ans, used)
                used[i] = 0