# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:    
        if not root: 
            return True
        else:
            return self.helper(root) != -1
        
    def helper(self, node):
        if not node:
            return 0
        left  = self.helper(node.left)
        right = self.helper(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) >= 2:
            return -1
        else:
            return max(left, right) + 1 