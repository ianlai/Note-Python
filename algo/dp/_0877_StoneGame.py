# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         if piles is None or len(piles) == 0:
#             return False
        
#         return self.helper(piles, 0, 0, True)
    
#     def helper(self, piles, mine, yours, isMyTurn):
#         #print("mine:", mine, " yours:", yours)
#         if len(piles) == 0:
#             if mine > yours:
#                 return True
#             return False
        
#         if isMyTurn == True:
#             selectFront = self.helper(piles[1:], mine + piles[0], yours, False)
#             selectBack  = self.helper(piles[:len(piles)-1], mine + piles[-1], yours, False)
#             return selectFront or selectBack
#         else:
#             selectFront = self.helper(piles[1:], mine, yours + piles[0], True)
#             selectBack  = self.helper(piles[:len(piles)-1], mine, yours + piles[-1], True)
#             return selectFront or selectBack
        
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         if piles is None or len(piles) == 0:
#             return False
#         memo = {}
#         return self.helper(piles, 0, len(piles)-1, 0, 0, True, memo)
    
#     def helper(self, piles, i, j, mine, yours, isMyTurn, memo):
#         #print("mine:", mine, " yours:", yours)
#         if i == j:
#             if mine > yours:
#                 return True
#             return False
#         if (i, j, mine, yours, isMyTurn) in memo:
#             return memo[(i, j, mine, yours, isMyTurn)]

#         if isMyTurn == True:
#             selectFront = self.helper(piles, i + 1, j, mine + piles[i], yours, False, memo)
#             selectBack  = self.helper(piles, i, j - 1, mine + piles[j], yours, False, memo)
            
#         else:
#             selectFront = self.helper(piles, i + 1, j, mine, yours + piles[i], True, memo)
#             selectBack  = self.helper(piles, i, j - 1, mine, yours + piles[j], True, memo)
    
#         memo[(i, j, mine, yours, isMyTurn)] = selectFront or selectBack
#         return memo[(i, j, mine, yours, isMyTurn)] 
    

# Top-Down (memoization)
class Solution:
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

# from functools import lru_cache
# class Solution:
#     def stoneGame(self, piles):
#         N = len(piles)

#         @lru_cache(None)
#         def dp(i, j):
#             # The value of the game [piles[i], piles[i+1], ..., piles[j]].
#             if i > j: return 0
#             parity = (j - i - N) % 2
#             if parity == 1:  # first player
#                 return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
#             else:
#                 return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

#         return dp(0, N - 1) > 0