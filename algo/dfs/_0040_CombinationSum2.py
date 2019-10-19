class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None and len(candidates) == 0:
            return []
        
        candidates = sorted(candidates)
        print(candidates)
        ans = set()
        
        self.dfs(ans, candidates, [], -1, target)
        return list(ans)
    
    def dfs(self, ans, candidates, cur, index, target):
        #print(cur , ": ", target)
        if target < 0:
            return 
        if target == 0: 
            #ans.add(cur)  #unhashable type: 'list'
            ans.add(tuple(cur))
            return 
        
        for i in range(index + 1, len(candidates)):            
            self.dfs(ans, candidates, cur + [candidates[i]], i, target - candidates[i])
        