# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        
        arr = []
        self.traverse(root, arr)
        
        min = float('inf')
        for i in range(1, len(arr)):
            cur = arr[i] - arr[i-1] 
            min = cur if cur < min else min
        
        return min
    
    def traverse(self, node, arr):
        if node is None:
            return 
        self.traverse(node.left, arr)
        arr.append(node.val)
        self.traverse(node.right, arr)
    