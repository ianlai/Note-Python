class Solution:

    # Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
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
                
        