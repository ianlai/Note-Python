# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.helper(root.left, root.right):
            return False
        return True
    def helper(self, left, right) -> bool:
        # both null
        if not left and not right: 
            return True
        # right null
        if left and not right: 
            return False
        # left null
        if not left and right: 
            return False
        # both not null
        print(left.val, right.val)
        if left.val == right.val:       
            if not self.helper(left.left, right.right):
                return False
            if not self.helper(left.right, right.left):
                return False
            return True
        else:
            return False