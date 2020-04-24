import heapq
class Solution:
    
    #Use Heap [5%]
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k <= 0:
            return []
        if k == 1:
            return nums
        
        ans = []
        p1, p2 = 0, k
        window = nums[p1:p2]
        window = [-x for x in window]
        heapq.heapify(window)
        
        while True:
            #print(p1, p2-1, window)
            
            minValue = window[0] #get min
            maxValue = -minValue
            ans.append(maxValue)
            
            
            if p2 < len(nums):
                # remove first (nums) in window
                removeElement = -nums[p1]
                removeIdx = window.index(removeElement)
                window[removeIdx] = window[-1] 
                window.pop()  #pop last
                
                # add new
                heapq.heappush(window, -nums[p2])
 
                # heapify window 
                heapq.heapify(window)
                p1 += 1
                p2 += 1
            else:
                break
                
        return ans 
            