# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Stack [12%-91%]
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return root
        
        res = []
        stack = []
        
        stack.append(root)
        
        while(stack):
            cur = stack.pop()
            res.append(cur.val)          #(1)middle 
            if cur.right:
                stack.append(cur.right)  #(3)right
            if cur.left:
                stack.append(cur.left)   #(2)left 
        
        return res