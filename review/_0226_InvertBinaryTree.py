# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Practice 2
    def invertTree(self, root: TreeNode) -> TreeNode:
        print("2")
        if not root:
            return None
        left = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = left
        return root

            
    #Practice 1         
    def invertTree1(self, root: TreeNode) -> TreeNode:
        print("1")
        if not root: 
            return root
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left  = temp
        return root