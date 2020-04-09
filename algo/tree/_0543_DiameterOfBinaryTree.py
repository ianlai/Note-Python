# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Array to store answer 
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = [0] 
        self.maxDepth(root, ans)
        return ans[0]
    
    def maxDepth(self, root, ans):
        if root is None:
            return 0 
        left = self.maxDepth(root.left, ans)
        right= self.maxDepth(root.right, ans)
        ans[0] = max(ans[0], left + right)
        return 1 + max(left, right)
    
    # Global variable to store answer 
    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        def maxDepth(root):
            if root is None:
                return 0 
            left = maxDepth(root.left)
            right= maxDepth(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
    
        if root is None:
            return 0
        self.ans = 0  #global variable 
        maxDepth(root)
        return self.ans
    
