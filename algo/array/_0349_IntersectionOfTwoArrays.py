class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        setIntersection = set()
        for e in nums1:
            set1.add(e)
        for e in nums2:
            if e in set1:
                setIntersection.add(e)
        ans = list(setIntersection)
        return ans
            