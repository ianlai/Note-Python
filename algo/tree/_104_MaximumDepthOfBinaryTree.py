# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return self.helper(root, 0)
    def helper(self, root, depth):
        if not root:
            return depth
        else:
            left_depth = self.helper(root.left, depth+1)
            right_depth = self.helper(root.right, depth+1)
            return max(left_depth, right_depth)
            
        