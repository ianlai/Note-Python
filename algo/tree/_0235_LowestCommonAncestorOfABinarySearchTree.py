# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive [17% - 39%]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        
        if (root.val == p.val 
            or (root.val == q.val) 
            or (p.val > root.val and q.val < root.val) 
            or (p.val < root.val and q.val > root.val)):
            return root
        
        if p.val > root.val: #go right
            return self.lowestCommonAncestor(root.right, p, q)
        else:                #go left
            return self.lowestCommonAncestor(root.left, p, q)