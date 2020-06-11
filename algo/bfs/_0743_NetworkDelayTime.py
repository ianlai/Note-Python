class Solution:
    
    #BFS with Priority Queue [O(VlogV), 7%]
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times: 
            return 0
        
        timeMap = {}     #map ID to children array 
        timeSet = set()  #avoid redundancy
        for t in times:
            timeMap[t[0]] = timeMap.get(t[0], []) + [[t[1], t[2]]]
            
            ## This code is also fine: 
            # if t[0] not in timeMap:
            #     timeMap[t[0]] = []
            # timeMap[t[0]].append([t[1], t[2]])
            
        print(timeMap)
        
        pq = [[0, K]]  #distance, ID 
        count = 0 
        while pq:
            heapq.heapify(pq)
            cur = heapq.heappop(pq)
            
            #(1): Visited check (since we sort use heap to sort it, we don't need to go to same nodes again)
            if cur[1] in timeSet:
                continue
            timeSet.add(cur[1])
            
            #(2): If all nodes are visited, we can just return 
            if len(timeSet) == N:
                return cur[0]
            
            #(3): (1) and (2) are passed. Check the map to see the node has a children array or not. 
            if cur[1] not in timeMap: 
                continue
                
            curList = timeMap[cur[1]]
            for t in curList: 
                heapq.heappush(pq, [cur[0] + t[1], t[0]])   
        return -1