
class Solution:
    
    # Use Array, O(1) space  [93%]
    def findDuplicate(self, nums: List[int]) -> int:
        print("Array")
        if not nums:
            return -1
        for e in nums:
            e = abs(e)
            idx = e - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                return e
    
    # Use Map, O(n) space  [93%]
    def findDuplicate1(self, nums: List[int]) -> int:
        print("Map")
        if not nums:
            return -1
        count = collections.Counter(nums)
        for e in count:
            if count[e] > 1:
                return e