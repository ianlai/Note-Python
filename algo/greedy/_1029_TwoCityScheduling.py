class Solution:
    
    # Greedy, but why? [O(nlogn), 11%]
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        diffs = [[p[0]-p[1], p] for p in costs]
        diffs.sort(key = lambda x: x[0])
        
        # start, end = 0, len(costs)-1
        ans = 0
        
        for i in range(len(costs)):
            if i < len(costs)/2:
                ans += diffs[i][1][0]
            else:
                ans += diffs[i][1][1]

        return ans
    
        # prev = 0
        # firstPositiveIdx = 0
        # for i in range(len(costs)):
        #     if diffs[i][0] < 0 :
        #         ans += diffs[i][1][0]
        #         prev = diffs[i][0]
        #     else:
        #         if prev < 0:
        #             firstPositiveIdx = i
        #         ans += diffs[i][1][0]
        
        
        
        
            