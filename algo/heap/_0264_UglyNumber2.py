import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 1:
            return -1
        if n == 1:
            return 1
    
        base = [2, 3, 5]
    
        map  = {2, 3, 5}
        heap = [2, 3, 5]
        heapq.heapify(heap)
        
        min = 0
        for i in range(n-1):
            #min = heap[0]
            min = heapq.heappop(heap) #remove from heap
            map.remove(min)           #remove from map
            for e in base:
                new = min * e
                if new not in map:
                    map.add(new)
                    heapq.heappush(heap, new)
                #print(min, " x ", e, " -> ", map)
        
        return min
    
