class Solution:
    def countArrangement(self, N: int) -> int:
        if N <= 0: 
            return 0
        
        #create array
        arr = [e + 1 for e in range(N)]
        ans = []
        used = [0] * N
        
        #beautiful permute
        self.beautifulPermute(arr, [], 0, used, ans)
        
        #print(ans)
        return len(ans)
        
    def beautifulPermute(self, arr, cur, idx, used, ans):
        if len(cur) == len(arr):
            #check beautiful in the end (TLE)
            #if self.isBeautiful(cur):
                #ans.append(cur)
            #ans[0] = ans[0] + 1
            ans.append(cur)
            return 
       
        # check beautiful on the way (OK)
        if not self.isCurBeautiful(cur + [arr[idx]]):
            return
        
        for i in range(len(arr)):
            if used[i] == 0:
                used[i] = 1
                self.beautifulPermute(arr, cur + [arr[i]], i, used, ans)
                used[i] = 0
    
    def isCurBeautiful(self, cur):
        if cur[-1] % len(cur) != 0 and len(cur) % cur[-1] != 0:
            return False
        return True
    
    def isBeautiful(self, cur):
        for i in range(len(cur)):
            if cur[i] % (i+1) != 0 and (i+1) % cur[i] != 0:
                return False
        return True