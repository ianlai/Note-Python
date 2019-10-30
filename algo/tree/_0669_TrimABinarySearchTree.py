# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val > R:  #trim (too high)
            root = self.trimBST(root.left, L, R)
                
        elif root.val < L:  #trim (too low)
            root = self.trimBST(root.right, L, R)

        else:  #keep 
            if root.left:
                root.left = self.trimBST(root.left, L, R)        
            if root.right:
                root.right = self.trimBST(root.right, L, R)

        return root