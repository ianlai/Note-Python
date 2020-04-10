class Solution:
    
    # Naive approach: O(log(m+n))  (43%)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1, i2 = 0, 0
        nums3 = []
        while True:
            if i1 == len(nums1):
                nums3.extend(nums2[i2:])
                break
            if i2 == len(nums2):
                nums3.extend(nums1[i1:])
                break
            if nums1[i1] < nums2[i2]:
                nums3.append(nums1[i1])
                i1 += 1
            else:
                nums3.append(nums2[i2])
                i2 += 1
        
        ans = 0
        if len(nums3) % 2 == 0:
            index = len(nums3) // 2 
            ans = (nums3[index-1] + nums3[index]) / 2
        else:
            index = len(nums3) // 2 
            ans = nums3[index]
        
        return ans
            