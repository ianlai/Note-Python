class Solution:
        
    # Two pointers  
    def intersectTwoPointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        ans = []
        
        idx1, idx2 = 0, 0
        while idx1 != len(nums1) and idx2 != len(nums2):
            if nums1[idx1] == nums2[idx2]:
                ans.append(nums1[idx1])
                idx1 += 1
                idx2 += 1  
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
        return ans
            
    
    # Count with dictionary 
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        ans = []
        for e in nums1:
            if e in count.keys():
                count[e] += 1
            else:
                count[e] = 1
        for e in nums2:
            if e in count.keys() and count[e] > 0:
                ans.append(e)
                count[e] -= 1
        return ans
                
                