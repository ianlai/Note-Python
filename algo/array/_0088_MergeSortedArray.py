class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1 
        
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
            
        #add missing elements from nums2
        if p1 < 0:
            for i in range(p3+1):
                nums1[i] = nums2[i]
            return
            
        return 