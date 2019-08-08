# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return self.helper(root)
    def helper(self, node):
        if node.left is None and node.right is None:
            return 1
        if node.left and node.right:  
            return 1 + min(self.helper(node.left), self.helper(node.right))
        if node.left: 
            return 1 + self.helper(node.left)
        if node.right: 
            return 1 + self.helper(node.right)
        