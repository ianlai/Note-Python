from collections import deque
class Solution:
    
    # ================================    
    # Version 2 (Jiuzhang, modulized)
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr is None or len(arr) == 0:
            return arr
        
        right = self.findUpperSmallest(arr, x)
        left = right - 1
        #print(left, right)
        ans = []
        
        # Input k elements
        for _ in range(k):
            if self.isLeftCloser(arr, x, left, right):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        ans.sort()
        return ans
    
    def findUpperSmallest(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end: 
            mid = (start + end) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid 
        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end
        return end + 1  #upper smallest 
    
    def isLeftCloser(self, arr, x, left, right):
        if left < 0 :
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x
        
    # ================================    
    # Version 1 (messy)
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr is None or len(arr) == 0:
            return arr
        
        start, end = 0, len(arr) - 1
        ans = deque([])

        minDiffIdx = 0 
        # Step1: Find min diff index (Binary Search)
        while start + 1 < end:
            mid = int((start + end) / 2)
            diff = arr[mid] - x
            #print(arr[mid], diff)
            if diff == 0: 
                minDiffIdx = mid
                break
            elif diff > 0 :
                end = mid 
            elif diff < 0 :
                start = mid
        
        if abs(arr[start] - x) <= abs(arr[end] - x): #including eqal
            minDiffIdx = start 
        else:
            minDiffIdx = end 
            
        #print("minDiffIdx:", minDiffIdx)
        #print("minDiffEle:", arr[minDiffIdx])
        
        # Step2: Input k elements
        ans.append(arr[minDiffIdx])
        left = minDiffIdx - 1
        right = minDiffIdx + 1
        last = len(arr) - 1 
        
        for i in range(k-1):
            if left < 0 and right > last:
                return ans  # not filled up yet but no more
            elif left < 0:
                ans.append(arr[right])
                right += 1
            elif right > last:
                ans.appendleft(arr[left])
                left -= 1
            else:           #compare to fill in
                if abs(arr[left] - x) <= abs(arr[right] - x): #including equal
                    ans.appendleft(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right +=1 
        return ans
                
            
        
                
            