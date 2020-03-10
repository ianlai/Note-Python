# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, i, j) -> TreeNode:
        if i > j:
            return None
        mid = (i + j) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, i, mid - 1)
        node.right = self.helper(nums, mid + 1, j)
        
        return node 
        