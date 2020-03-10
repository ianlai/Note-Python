# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # if root finds both p and q    -> return root 
    # if root finds only p          -> return p
    # if root finds only q          -> return q
    # if root finds neither p nor q -> return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q: 
            return root
        
        left  = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is None and right is None: #both left and right don't have p or q 
            return None
        if left is None:  #right has p or q 
            return right 
        if right is None: #left has p or q
            return left
        return root       #both left and right have p or q 