class Solution:
    
    #Dijkstra [time: O(ElogV), 32%]
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        print("Dijkstra")
        if not times:
            return 0
        distance = [float('inf')] * (N + 1)
        distance[0] = 0
        #distance[K] = 0   #This is different from Bellman-Ford's one (can't continue if we have this)
        
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w 
        
        heap = [(0, K)]  #only one so we don't need to heapify it
        while heap:
            dist, u = heapq.heappop(heap)
            if distance[u] != float('inf'): #Remove the redundancy 
                continue
            distance[u] = dist
            
            for v in weight[u]:
                heapq.heappush(heap, (distance[u] + weight[u][v], v))
        
        if max(distance) == float('inf'):
            return -1
        return max(distance)
            
    #=================================================================
    #Bellman-Ford [time: O(EV), 21%]
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        print("Bellman-Ford")
        if not times: 
            return 0
        distance = [float('inf')] * (N + 1)
        distance[0] = 0
        distance[K] = 0
        
        for _ in range(N-1):  #|V|-1 times 
            for u, v, w in times: 
                if distance[v] > distance[u] + w: #
                    distance[v] = distance[u] + w
                    
        if max(distance) == float('inf'):
            return -1
        return max(distance)
                    
    #=================================================================
    
    #BFS with Priority Queue [O(VlogV), 7%]
    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        print("BFS + Priority Queue")
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
            
            #(1): Visited check (since we use heap to sort it, we don't need to go to same nodes again)
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