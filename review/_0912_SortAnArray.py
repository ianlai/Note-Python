isDebug = False
class Solution:

    def debug(self, *argv):
        if not isDebug:
            return 
        for arg in argv:
            print(arg, end=" ")
        print()

    # Quick sort (seprate partition and recursive function) [53%]
    def sortArray2(self, nums: List[int]) -> List[int]:
        print("Quick Sort 1 (separate)")
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def quickSort(self, nums, s, e):
        self.debug()
        self.debug("s, e:", s, e)
        if s >= e:
            return 
        left, right = self.partition(nums, s, e)
        self.debug("left :", s, right)
        self.debug("  right:", left, e)
        self.quickSort(nums, s, right)  #[start to right] (since right comes to left already) 
        self.quickSort(nums, left, e)    #[left to end]    (since left comes to right already)
    
    # partition function is to find right, left indices (actually it's one partition point)
    def partition(self, nums, s, e):
        pivot = nums[(s+e)//2]  #we don't care pivot's index
        left, right = s, e
        while left <= right:     #seems either "<" or "<=" is fine (but inner ones need to be "<="")
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:   #index, not value (final check before swapping)
                nums[left], nums[right] = nums[right], nums[left] #swap 
                left += 1
                right -= 1
        self.debug("pivot:", pivot)
        self.debug(nums)
        self.debug("partition:", left, right)

        return left, right
    #=====================================================
    
    # Quick sort (Jiuzhang) [62%]
    # >> Put partition function in quickSort function
    def sortArray2(self, nums: List[int]) -> List[int]:
        self.debug("Quick Sort 2 (combined)")
        def quickSort(nums, s, e):
            self.debug()
            self.debug("s, e:", s, e)
            if s >= e:
                return 
            pivot = nums[(s+e)//2]  #we don't care pivot's index
            left, right = s, e
            while left <= right:     #seems either "<" or "<=" is fine (but inner ones need to be "<="")
                while left <= right and nums[left] < pivot:
                    left += 1
                    self.debug("L")
                while left <= right and nums[right] > pivot:
                    right -= 1
                    self.debug("R")
                if left <= right:   #index, not value (final check before swapping)
                    nums[left], nums[right] = nums[right], nums[left] #swap 
                    left += 1
                    right -= 1
                    self.debug("LR")
            self.debug("pivot:", pivot)
            self.debug(nums)
            self.debug("partition:", left, right)

            self.debug("left :", s, right)
            self.debug("  right:", left, e)
            self.debug()
            quickSort(nums, s, right)  #[start to right] (since right comes to left already) 
            quickSort(nums, left, e)   #[left to end]    (since left comes to right already)
        quickSort(nums, 0, len(nums)-1)
        return nums
    
    #=====================================================
    
    # Merge Sort: python slice approach  [16% - 37%] 
    def sortArray2(self, nums: List[int]) -> List[int]:
        print("Merge Sort 1 (slice)")
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left  = self.sortArray(nums[:mid])  #return a sorted subarry
        right = self.sortArray(nums[mid:])  #return a sorted subarry
        return self.merge(left, right)
    
    # merge two subarrays, e.g. [1,4,5] [2,3,6] -> [1,2,3,4,5,6]
    # create a new array to store the sorted subarray (that's why merge sort space is O(n))
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
        res.extend(left[left_cur:])   #put the remaining if there is any
        res.extend(right[right_cur:]) #put the remaining if there is any
        return res
    
    #=====================================================

    # Merge Sort: index approach  [25%]
    def sortArray(self, nums: List[int]) -> List[int]:
        print("Merge Sort 2 (index)")
        def merge(nums, s, e, res):
            mid = (s + e) // 2
            left_cur, right_cur = s, mid + 1 #left: s to mid ; right mid+1 to e 
            index = s
            while left_cur <= mid and right_cur <= e:
                if nums[left_cur] < nums[right_cur]:
                    #self.debug("left:", nums[left_cur])
                    res[index] = nums[left_cur]
                    left_cur += 1
                else:
                    #self.debug("right:", nums[right_cur])
                    res[index] = nums[right_cur]
                    right_cur += 1
                index += 1
                
            while left_cur <= mid:
                #self.debug("end-left:", nums[left_cur])
                res[index] = nums[left_cur]
                left_cur += 1
                index += 1
                
            while right_cur <= e:
                #self.debug("end-right:", nums[right_cur])
                res[index] = nums[right_cur]
                right_cur += 1
                index += 1
                
            # deep copy ; keep nums the same id 
            for i in range(s, e + 1):
                nums[i] = res[i]
            #self.debug(nums)
        
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