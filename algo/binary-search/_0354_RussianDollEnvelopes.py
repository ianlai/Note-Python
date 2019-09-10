from typing import List
class Solution:       
    
    # Binary Search
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        if e is None or len(e) == 0:
            return 0
        e.sort(key=lambda x: [x[0], -x[1]])
        #print("arr: ", e)
        
        tails = [0]
        tails[0] = e[0]
        
        for i in range (1, len(e)):
            x = e[i]
            
            # Binary Search
            start, end = 0, len(tails) - 1
            mid = -1
            while start + 1 < end:
                mid = (start + end) // 2
                #print(start, mid, end)
                if tails[mid-1][1] < x[1] <= tails[mid][1]:
                    tails[mid] = x
                    break
                elif x[1] > tails[mid][1]:
                    start = mid 
                elif x[1] <= tails[mid-1][1]:
                    end = mid 

            if tails[mid] == x:
                #print("x:", x, " -- ", tails)
                continue
            if x[1] <= tails[start][1]:
                tails[start] = x
            elif tails[start][1]< x[1] <= tails[end][1]:
                tails[end] = x
            else:
                tails.append(x)

            #print("x:", x, " -- ", tails)
            
        return len(tails)
    
    # DP 
    def maxEnvelopes_DP(self, envelopes: List[List[int]]) -> int:
        if envelopes is None or len(envelopes) == 0:
            return 0
        envelopes = sorted(envelopes) #sort the first element then the second element
        #print(envelopes)
        
        lis = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    lis[i] = max(lis[i], lis[j] + 1)
        #print(lis)
        
        return max(lis)

sol = Solution()
env1 = [[5,4],[6,4],[6,7],[2,3],[2,7],[6,5],[5,1],[3,2],[6,8],[7,8]]
env2 = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
env3 = [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
env4 = [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]]
env5 = [[33,23],[43,3],[10,43],[42,29],[5,34],[41,14],[40,14],[5,37],[25,6],[7,2],[34,47],[46,40],[7,6],[41,40],[16,36],[41,30],[18,31],[21,42],[10,5],[40,29],[8,12],[36,13],[47,8],[3,8],[38,18],[2,48],[15,29],[17,4],[30,47],[32,36],[8,49],[11,41],[34,22],[1,48],[4,1],[42,35],[33,9],[3,16],[29,30],[18,13],[30,11],[6,43],[4,16],[32,15],[11,50],[13,21],[40,28],[36,21],[39,26],[32,31],[25,8],[40,28],[30,22],[20,42],[43,18],[19,40],[45,9],[50,12],[50,38],[41,27],[47,14],[8,39],[40,45],[38,34],[33,5],[14,37],[35,15],[7,6],[38,47],[43,46],[30,29],[36,49],[4,18],[28,47],[50,31],[10,34],[40,31]]
print("DP: ", sol.maxEnvelopes_DP(env1))
print("BS: ", sol.maxEnvelopes(env1))

print("DP: ", sol.maxEnvelopes_DP(env2))
print("BS: ", sol.maxEnvelopes(env2))

print("DP: ", sol.maxEnvelopes_DP(env3))
print("BS: ", sol.maxEnvelopes(env3))

print("DP: ", sol.maxEnvelopes_DP(env4))
print("BS: ", sol.maxEnvelopes(env4))

print("DP: ", sol.maxEnvelopes_DP(env5))
print("BS: ", sol.maxEnvelopes(env5))