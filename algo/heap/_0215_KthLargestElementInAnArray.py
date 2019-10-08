class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return self.findKthLargest_MinHeap(nums, k)
        return self.findKthLargest_MaxHeap(nums, k)
    
    # Max Heap 
    def findKthLargest_MaxHeap(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        nums = [-x for x in nums]
        heapq.heapify(nums)
        result = 0
        for i in range(k):
            result = heapq.heappop(nums)
        return -result
    
    # Min Heap 
    def findKthLargest_MinHeap(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        sub = nums[:k]
        heapq.heapify(sub)
        for i in range(k, len(nums)):
            #print(i, " ", sub)
            min = sub[0] 
            if nums[i] > min:  #replace the min
                heapq.heappop(sub)
                heapq.heappush(sub, nums[i])
        return sub[0]
        