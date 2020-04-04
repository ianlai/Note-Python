class Solution:
    
    # Quick sort (62%)
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, s, e):
            if s >= e:
                return 
            pivot = nums[(s+e)//2]  #we don't care pivot's index
            left, right = s, e
            while left <= right:
                while left <= right and nums[left] < pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left] #swap 
                    #print("swap:", left, right)
                    left += 1
                    right -= 1
            quickSort(nums, s, right)
            quickSort(nums, left, e)
        quickSort(nums, 0, len(nums)-1)
        return nums
    
    # Merge Sort: python slice approach  (16%) 
    def sortArray1(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        left_cur, right_cur = 0, 0 
        res = []
        while left_cur < len(left) and right_cur < len(right):
            if left[left_cur] < right[right_cur]:
                res.append(left[left_cur])
                left_cur += 1
            else:
                res.append(right[right_cur])
                right_cur += 1
        res.extend(left[left_cur:])
        res.extend(right[right_cur:])
        return res
    
    
    # Merge Sort: index approach 
    def sortArray2(self, nums: List[int]) -> List[int]:
        def merge(nums, s, e, res):
            #print("-------------")
            #print(nums)
            #print("s:", s, "e:", e)
            mid = (s + e) // 2
            left_cur, right_cur = s, mid + 1 #left: s to mid ; right mid+1 to e 
            #print("L:", left_cur, "R:", right_cur)
            index = s
            
            while left_cur <= mid and right_cur <= e:
                if nums[left_cur] < nums[right_cur]:
                    #print("left:", nums[left_cur])
                    res[index] = nums[left_cur]
                    left_cur += 1
                else:
                    #print("right:", nums[right_cur])
                    res[index] = nums[right_cur]
                    right_cur += 1
                index += 1
                
            while left_cur <= mid:
                #print("end-left:", nums[left_cur])
                res[index] = nums[left_cur]
                left_cur += 1
                index += 1
                
            while right_cur <= e:
                #print("end-right:", nums[right_cur])
                res[index] = nums[right_cur]
                right_cur += 1
                index += 1
                
            # deep copy ; keep nums the same id 
            for i in range(s, e + 1):
                nums[i] = res[i]
            #print(nums)
        
        def mergeSort(nums: List[int], s: int, e: int, res: List[int]):
            if s >= e:
                return
            mid = (s + e) // 2
            mergeSort(nums, s, mid, res)
            mergeSort(nums, mid+1, e, res)
            merge(nums, s, e, res)
            
        res = [0] * len(nums)
        mergeSort(nums, 0, len(nums)-1, res)
        return res