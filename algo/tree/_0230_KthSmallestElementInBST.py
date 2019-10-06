# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return -1
        
        arr = []
        self.traverse(root, arr)
        return arr[k-1]
            
    def traverse(self, node, arr):
        if node is None:
            return 
        
        self.traverse(node.left, arr)
        arr.append(node.val)
        self.traverse(node.right, arr)
        return