# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        arr = []
        self.inorderTraverse(root, arr)
        
        minDiff = float('inf')
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i] - arr[i-1])
        return minDiff
    
    def inorderTraverse(self, node, arr):
        if not node:
            return
        self.inorderTraverse(node.left, arr)
        arr.append(node.val)
        self.inorderTraverse(node.right, arr)