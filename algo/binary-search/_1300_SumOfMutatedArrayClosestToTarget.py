class Solution:        
    
        # Binary search (twice)
        # Step1: Sort
        # Step2: Find the interval [0, 20204] or [20204, 25176] or [25176, 60864]
        #               min            max
        #       0 ..... 20204, 25176, 60864 
        # Step3: Find the val in the interval 
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort()
        start, end = 0, arr[-1]
        visited = set()

        idx = 0
        while True:
            val = arr[idx]
            res = self.cal(arr, val)
            #print(val, ":", res)
            
            if idx >= len(arr): 
                return res
            elif idx < 0:
                return self.binarySearch(arr, 0, arr[0], target)            
            else:
                if res < target:
                    if idx in visited:
                        return self.binarySearch(arr, arr[idx], arr[idx+1], target)
                    visited.add(idx)
                    idx += 1 
                    
                elif res > target:
                    if idx in visited:
                        return self.binarySearch(arr, arr[idx-1], arr[idx], target)
                    visited.add(idx)
                    idx -= 1 
                else:
                    return val
    
    def binarySearch(self, arr, start, end, target):
        #print("  bs:", start, end, target)
        left, right = start, end 
        while left + 1 < right:
            val = (left + right) // 2
            res = self.cal(arr, val)
            if res < target:
                left = val
            elif res > target:
                right = val
            else:
                return val
        
        if target - self.cal(arr, left) <= self.cal(arr, right) - target:
            return left
        else:
            return right 
        
    def cal(self, arr, val):
        ans = 0
        for e in arr:
            if e > val:
                ans += val
            else:
                ans += e
        return ans 
        