class Solution:
    # heapq     
    def lastStoneWeight(self, stones: List[int]) -> int:
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