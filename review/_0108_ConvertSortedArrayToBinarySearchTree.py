# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Practice-2 (2020.08.02)
    # Pass the sub-array [O(n), 56%]
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        print("Practice-2")
        if not nums:
            return None
        
        middleIdx = (len(nums) - 1 )// 2
        root = TreeNode(nums[middleIdx]) 
        root.left  = self.sortedArrayToBST(nums[:middleIdx])
        root.right = self.sortedArrayToBST(nums[middleIdx+1:])
        return root
    
    #========================================================
    
    # Practice-1 (2020.03.10)
    # Pass the whole array [O(n), 89%]
    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        print("Practice-1")
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, i, j) -> TreeNode:
        if i > j:
            return None
        mid = (i + j) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, i, mid - 1)
        node.right = self.helper(nums, mid + 1, j)
        
        return node 
        