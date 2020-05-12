
class Solution:
    
    # heapq [75%]
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative = [-x for x in stones]
        heapq.heapify(negative)
        while len(negative) > 1:
            diff = -(heapq.heappop(negative)) + heapq.heappop(negative)
            if diff > 0:
                heapq.heappush(negative, -diff)
        if negative: 
            return -negative[0]
        return 0
            
        
    
    # heapq     
    def lastStoneWeight1(self, stones: List[int]) -> int:
        if stones is None:
            return -1
        negative_stones = [-x for x in stones]        
        heapq.heapify(negative_stones)  #heapfiy with negative elements
        while len(negative_stones) >= 2:
            #print(negative_stones)
            max1 = heapq.heappop(negative_stones)
            max2 = heapq.heappop(negative_stones)
            leftover = abs(max1 - max2) 
            heapq.heappush(negative_stones, -leftover)
        return -negative_stones[0]