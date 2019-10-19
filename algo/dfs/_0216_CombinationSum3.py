class Solution:
    
    # no duplication in the base arrary
    # no duplication in each comination array
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 and n == 0:
            return []
        if k == 0 and n != 0:
            return None
        if k != 0 and n == 0:
            return None
        
        base = [1,2,3,4,5,6,7,8,9]
        ans = []
        self.dfs(base, ans, k, n, [], -1)
        return ans
    
    def dfs(self, base, ans, length, target, cur, index):
        if len(cur) == length:
            if target == 0:
                ans.append(cur)
                return 
        for i in range(index + 1, len(base)):
            self.dfs(base, ans, length, target-base[i], cur + [base[i]], i)
        
            
    