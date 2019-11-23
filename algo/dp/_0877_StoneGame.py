from typing import List 
import time

# Complex Recursion (parameters: pile + 3 parameters)
class Solution_Complex_Recursion:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        
        return self.helper(piles, 0, 0, True)
    
    def helper(self, piles, mine, yours, isMyTurn):
        #print("mine:", mine, " yours:", yours)
        if len(piles) == 0:
            if mine > yours:
                return True
            return False
        
        if isMyTurn == True:
            selectFront = self.helper(piles[1:], mine + piles[0], yours, False)
            selectBack  = self.helper(piles[:len(piles)-1], mine + piles[-1], yours, False)
            return selectFront or selectBack
        else:
            selectFront = self.helper(piles[1:], mine, yours + piles[0], True)
            selectBack  = self.helper(piles[:len(piles)-1], mine, yours + piles[-1], True)
            return selectFront or selectBack

#==============================================================================

# Complex Memoization (parameters: pile + 5 parameters + 1 memo list)
class Solution_Complex_Memoization:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        memo = {}
        return self.helper(piles, 0, len(piles)-1, 0, 0, True, memo)
    
    def helper(self, piles, i, j, mine, yours, isMyTurn, memo):
        #print("mine:", mine, " yours:", yours)
        if i == j:
            if mine > yours:
                return True
            return False
        if (i, j, mine, yours, isMyTurn) in memo:
            return memo[(i, j, mine, yours, isMyTurn)]

        if isMyTurn == True:
            selectFront = self.helper(piles, i + 1, j, mine + piles[i], yours, False, memo)
            selectBack  = self.helper(piles, i, j - 1, mine + piles[j], yours, False, memo)
            
        else:
            selectFront = self.helper(piles, i + 1, j, mine, yours + piles[i], True, memo)
            selectBack  = self.helper(piles, i, j - 1, mine, yours + piles[j], True, memo)
    
        memo[(i, j, mine, yours, isMyTurn)] = selectFront or selectBack
        return memo[(i, j, mine, yours, isMyTurn)] 

#==============================================================================

#Simplied Recursion (parameters: pile + 2 parameters)
class Solution_Simplified_Recursion:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        N = len(piles)
        return self.helper(piles, 0, N-1) > 0

    def helper(self, piles, i, j):
        if i > j: 
            return 0
        if (i + j) % 2 == 1:  # me 
            return max(piles[i] + self.helper(piles, i+1, j), piles[j] + self.helper(piles, i, j-1))             
        else:
            return min(-piles[i] + self.helper(piles, i+1, j), -piles[j] + self.helper(piles, i, j-1))        

#==============================================================================

#Simplied Recursion + Inner Function (parameters: 2 parameters)
class Solution_Simplified_Recursion_Inner:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        N = len(piles)

        def helper(i, j):
            if i > j: 
                return 0
            if (i + j) % 2 == 1:  # me 
                return max(piles[i] + helper(i+1, j), piles[j] + helper(i, j-1))             
            else:
                return min(-piles[i] + helper(i+1, j), -piles[j] + helper(i, j-1))   
        return helper(0, N-1) > 0

#==============================================================================

#Simplied Memoization + Inner Function (parameters: 2 parameters)
class Solution_Simplified_Memoization_Inner:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        N = len(piles)
    
        memo = {}
        def helper(i, j):

            if i > j: 
                return 0
            if (i,j) in memo:
                return memo[i,j]

            if (i + j) % 2 == 1:  # me 
                memo[i,j] = max(piles[i] + helper(i+1, j), piles[j] + helper(i, j-1))             
            else:
                memo[i,j] = min(-piles[i] + helper(i+1, j), -piles[j] + helper(i, j-1))   
            return memo[i,j]
        return helper(0, N-1) > 0
#==============================================================================

#Simplied Memoization (lru) + Inner Function  (parameters: 2 parameters)
from functools import lru_cache
class Solution_Simplified_Memoization_LRU_Inner:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        N = len(piles)

        @lru_cache(None)
        def helper(i, j):
            if i > j: 
                return 0
            if (i + j) % 2 == 1:  # me 
                return max(piles[i] + helper(i+1, j), piles[j] + helper(i, j-1))             
            else:
                return min(-piles[i] + helper(i+1, j), -piles[j] + helper(i, j-1))   
        return helper(0, N-1) > 0

#==============================================================================

#Simplied Memoization (lru) + Inner Function  (parameters: 2 parameters)
from functools import lru_cache
class Solution_Simplified_Memoization_LRU_Inner:
    def stoneGame(self, piles: List[int]) -> bool:
        if piles is None or len(piles) == 0:
            return False
        N = len(piles)

        @lru_cache(None)
        def helper(i, j):
            if i > j: 
                return 0
            if (i + j) % 2 == 1:  # me 
                return max(piles[i] + helper(i+1, j), piles[j] + helper(i, j-1))             
            else:
                return min(-piles[i] + helper(i+1, j), -piles[j] + helper(i, j-1))   
        return helper(0, N-1) > 0

#==============================================================================

#Math approach 
class Solution_Math:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

q1 = [5,3,2,7,9,6,7,10,15,27,43,64,25,35,22,12,32,13,16,18,14,37,58,24,28,36,21,15,37,18]
sols = [0] * 10

sols[0] = Solution_Complex_Recursion()
sols[1] = Solution_Complex_Memoization() 
sols[2] = Solution_Simplified_Recursion() 
sols[3] = Solution_Simplified_Recursion_Inner() 
sols[4] = Solution_Simplified_Memoization_Inner() 
sols[5] = Solution_Simplified_Memoization_LRU_Inner() 
sols[6] = Solution_Math() 

# print("Num of piles:", len(q1))
# for i in range(len(sols)):
#     sol = sols[i]
#     if sol == 0:
#         continue
#     t1 = time.time()
#     ans = sol.stoneGame(q1)
#     t2 = time.time()
#     elapsed = round(t2 - t1, 2)
#     print("[", i+1, "]", elapsed, sol.__class__.__name__, ": ", ans)

# Num of piles: 30
# [ 1 ] 971.84 Solution_Complex_Recursion :  True
# [ 2 ] 0.09 Solution_Complex_Memoization :  True
# [ 3 ] 831.34 Solution_Simplified_Recursion :  True
# [ 4 ] 822.21 Solution_Simplified_Recursion_Inner :  True
# [ 5 ] 0.0 Solution_Simplified_Memoization_Inner :  True
# [ 6 ] 0.0 Solution_Simplified_Memoization_LRU_Inner :  True
# [ 7 ] 0.0 Solution_Math :  True

# -------------------------------

q2 = [5,3,2,7,9,6,7,10,15,27,43,64,25,35,22,12,32,13,16,18,88,14,37,58,24,28,52,34,39,75,63,19,21,36,55,77,34,36,82,26,37,46,45,23,28,73,39,32,22,55,44,33,77,66,11,88,22,99,5,3,2,7,9,6,7,10,23,28,73,39,32,22,55,44,33,77,66,23,28,73,39,32,22,55,44,33,77,66,15,27,43,64,25,35,22,12,32,13,16,18,14,37,58,24,28,36, 55,77,34,36,82,26,37,46,45,23,28,73,39,32,22,55,44,33,77,66,11,88,22,99,5,3,2,7,9,6,7,10,15,27,43,64,25,35,22,12,32,13,16,18,14,37,58,24,28,36,55,77,34,36,82,26,37,46,45,23,28,73,39,32,22,55,44,33,77,66,11,88,22,99]
sols = [0] * 10

#sols[0] = Solution_Complex_Recursion() 
sols[1] = Solution_Complex_Memoization() 
#sols[2] = Solution_Simplified_Recursion() 
#sols[3] = Solution_Simplified_Recursion_Inner() 
sols[4] = Solution_Simplified_Memoization_Inner() 
sols[5] = Solution_Simplified_Memoization_LRU_Inner() 
sols[6] = Solution_Math() 

print("Num of piles:", len(q2))
for i in range(len(sols)):
    sol = sols[i]
    if sol == 0:
        continue
    t1 = time.time()
    ans = sol.stoneGame(q2)
    t2 = time.time()
    elapsed = round(t2 - t1, 3)
    print("[", i+1, "]", elapsed, sol.__class__.__name__, ": ", ans)

# Num of piles: 150
# [ 2 ] 33.717 Solution_Complex_Memoization :  True
# [ 5 ] 0.016 Solution_Simplified_Memoization_Inner :  True
# [ 6 ] 0.016 Solution_Simplified_Memoization_LRU_Inner :  True
# [ 7 ] 0.0 Solution_Math :  True

# Conclusion:
# Math > Simplifed Memoization LRU Inner > Simplifed Memoization Inner > Complex Memoization  
# >>>>> Simplified Recursion Inner > Simplified Recursion > Complex Recursion