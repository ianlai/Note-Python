class Solution:
    
    # Modified Dijkstra: [46% - 91%]
    # >> select smallest weight (heap nature), if no, next will be the larger weight but ok stops
    # Example:
    # 6
    # [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1],[5,1,2],[0,5,3]]
    # 0
    # 2
    # 2
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        print("Modified Dijkstra")
        if n == 0 or len(flights) == 0:
            return -1
        
        cost = collections.defaultdict(dict)
        for u, v, w in flights:
            cost[u][v] = w 
            
        distance = [float("inf") for _ in range(n)]
        curStops = [float("inf") for _ in range(n)]
        distance[src] = 0
        curStops[src] = 0
        
        heap = [(0, 0, src)]  #cost, stops, node
        
        while heap:
            #print("Heap:", heap, " Distance:", distance, "Stops:", curStops)
            c, s, u = heapq.heappop(heap)
            
            if u == dst:
                return c
            if s == K + 1:
                continue
            
            distance[u] = c  #MUST
            
            for v in cost[u]:
                #Consider the smallest weight path
                if distance[u] + cost[u][v] < distance[v]:
                    distance[v] = cost[u][v] + c
                    heapq.heappush(heap, (distance[v], s+1, v))
                
                #Also consider the path which has feasible stops yet (but not smallest weight)
                elif s < curStops[v]: 
                    curStops[v] = s
                    distance[v] = cost[u][v] + c
                    heapq.heappush(heap, (distance[v], s+1, v))
                    
                # Weight higher and step more (no need at all)
                # else:
                #     print("Not choosed:", [c, s ,u], "->", v)

        if distance[dst] != float("inf"):
            return distance[dst]
        return -1
    
    # ==================================================================================
    # Original Dijkstra (wrong) 
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        print("Original Dijkstra (wrong)")
        if n == 0 or len(flights) == 0:
            return -1
        
        cost = collections.defaultdict(dict)
        for u, v, w in flights:
            cost[u][v] = w 
            
        distance = {}
        heap = [(0, src)]
        count = 0
        while heap:
            print(count, heap, distance)
            for _ in range(len(heap)):
                c, u = heapq.heappop(heap)
                
                if u in distance:
                    continue
                
                distance[u] = c
                
                if count == K + 1:  #reach the question limit (K)
                    print("reach K:")
                    if dst in distance:
                        return distance[dst]
                    return -1 
                
                for v in cost[u]:
                    dist = c + cost[u][v]
                    heapq.heappush(heap, (dist, v))
            count += 1 
        
        print("empty heap")
        if dst in distance:
            return distance[dst]
        return -1 