import inspect
from typing import List
import time
class Solution:
    
    # (only this is correct) Use curIdx; use return value ; memoization ; remove the for loop
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        print(inspect.stack()[0][3])
        
        if nums is None or len(nums) == 0 :
            return 0 
        memo = {}  #key:(S, curIdx)
        self.dfs(nums, memo, S, 0, 0)
        return memo[(0, S)]
    
    def dfs(self, nums, memo, S, curIdx, i):
        tup = (curIdx, S)
        
        if tup in memo:
            #print(tup,",",memo[tup])
            return memo[tup]  #get
        
        if curIdx == len(nums):
            if S == 0:
                return 1
            return 0
        
        sum1, sum2 = 0, 0
        #for i in range(index + 1, len(nums)):   #remove this loop
        #print(S, "-", nums[i])
        sum1 = self.dfs(nums, memo, S - nums[i], curIdx + 1, i+1)
        #print(S, "+", nums[i])
        sum2 = self.dfs(nums, memo, S + nums[i], curIdx + 1, i+1)
        tup1, tup2 = (curIdx+1, S-nums[i]), (curIdx+1, S+nums[i])
        memo[tup1] = sum1 
        memo[tup2] = sum2
        memo[(curIdx, S)] = sum1+sum2
        #print("> add:", (curIdx, S),",",sum1 + sum2)

        return memo[(curIdx, S)]
    
    #=================================================
    
    # Use curIdx; use return value (not ans array)  
    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        print(inspect.stack()[0][3])
        
        if nums is None or len(nums) == 0 :
            return 0 
        
        return self.dfs2(nums, S, 0, -1)
    
    def dfs2(self, nums, S, curIdx, index):
        #print("index:", index, "S:", S)
        if curIdx == len(nums):
            if S == 0:
                return 1
            return 0
        
        sum = 0
        for i in range(index + 1, len(nums)):
            sum += self.dfs2(nums, S+nums[i], curIdx+1, i)
            sum += self.dfs2(nums, S-nums[i], curIdx+1, i)
        return sum
    
    #=================================================
    
    # Use curIdx; use ans array
    def findTargetSumWays3(self, nums: List[int], S: int) -> int:
        print(inspect.stack()[0][3])
        if nums is None or len(nums) == 0 :
            return 0 
        
        ans = [0]  #ans[0]
        
        self.dfs3(ans, nums, S, 0, -1)
        return ans[0]
    
    def dfs3(self, ans, nums, S, curIdx, index):
        #print("index:", index, "S:", S)
        if curIdx == len(nums):
            if S == 0:
                ans[0] += 1
            return
            
        for i in range(index + 1, len(nums)):
            self.dfs3(ans, nums, S + nums[i], curIdx+1, i)
            self.dfs3(ans, nums, S - nums[i], curIdx+1, i)
        return 
    
    #=================================================
    
    # Record cur[]
    def findTargetSumWays4(self, nums: List[int], S: int) -> int:
        print(inspect.stack()[0][3])
        if nums is None or len(nums) == 0 :
            return 0 
        
        ans = [0]  #ans[0]
        
        self.dfs4(ans, nums, S, [], -1)
        return ans[0]
    
    def dfs4(self, ans, nums, S, cur, index):
        if len(cur) == len(nums):
            if S == 0:
                ans[0] += 1
            return
            
        for i in range(index + 1, len(nums)):
            self.dfs4(ans, nums, S + nums[i], cur + [-nums[i]], i)
            self.dfs4(ans, nums, S - nums[i], cur + [nums[i]], i)
        return 

s = Solution() 
print(">>", s.findTargetSumWays([2,3,4], 9))
print(">>", s.findTargetSumWays2([2,3,4], 9))
print(">>", s.findTargetSumWays3([2,3,4], 9))
print(">>", s.findTargetSumWays4([2,3,4], 9))

print(">>", s.findTargetSumWays([1,1,2,2,3,3,3,1,1], 5))
print(">>", s.findTargetSumWays2([1,1,2,2,3,3,3,1,1], 5))
print(">>", s.findTargetSumWays3([1,1,2,2,3,3,3,1,1], 5))
print(">>", s.findTargetSumWays4([1,1,2,2,3,3,3,1,1], 5))

t11 = time.time()
print(">>", s.findTargetSumWays( [1,1,2,2,3,3,3,1,3,3,3,3,3,1,1], 5))
t12 = time.time()

t21 = time.time()
print(">>", s.findTargetSumWays2([1,1,2,2,3,3,3,1,3,3,3,3,3,1,1], 5)) #slow
t22 = time.time()

t31 = time.time()
print(">>", s.findTargetSumWays3([1,1,2,2,3,3,3,1,3,3,3,3,3,1,1], 5)) #slow
t32 = time.time()

t41 = time.time()
print(">>", s.findTargetSumWays4([1,1,2,2,3,3,3,1,3,3,3,3,3,1,1], 5)) #slow
t42 = time.time()

print('time elapsed 1: ' + str(round(t12-t11, 2)) + ' seconds')
print('time elapsed 2: ' + str(round(t22-t21, 2)) + ' seconds')
print('time elapsed 3: ' + str(round(t32-t31, 2)) + ' seconds')
print('time elapsed 4: ' + str(round(t42-t41, 2)) + ' seconds')

