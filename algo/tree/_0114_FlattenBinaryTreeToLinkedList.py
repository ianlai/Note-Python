# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    #pre-order flatten (central, left, right)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root) -> TreeNode:
        if root is None:
            return None
        if not root.left and not root.right:  #leaf node
            return root
            
        left_tail  = self.helper(root.left)
        right_tail = self.helper(root.right)
        
        if left_tail:      
            #connection adjustment 
            left_tail.right = root.right
            root.right = root.left 
            root.left = None
            
            #if right_tail exists, return right_tail 
            if right_tail:
                return right_tail
            else:
                return left_tail
        else:
            return right_tail
           
            
        
            
        