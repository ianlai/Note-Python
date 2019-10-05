# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, node: TreeNode, sum: int) -> bool:
        if node is None:
            return False
        sum -= node.val
        if node.left is None and node.right is None: 
            if sum == 0:
                return True
            else:
                return False
        if node.left is None:
            return self.hasPathSum(node.right, sum)
        if node.right is None:
            return self.hasPathSum(node.left, sum)
        return self.hasPathSum(node.left, sum) or self.hasPathSum(node.right, sum) 
            