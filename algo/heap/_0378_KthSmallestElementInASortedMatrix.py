import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0:
            return -1
        
        n = len(matrix) 
        
        heap = []
        heapq.heapify(heap) #not necessary 
        
        # (1) init (add first column into heap)
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))  #order matters, val needs to go first
        print(heap)
        print()
        
        # (2) heappop k time, add the next one if it exists
        point = None 
        for _ in range(k):
            point = heapq.heappop(heap)
            print(point)
            val, i, j = point[0], point[1], point[2]
            if j < n-1:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                
        return point[0]
            
            