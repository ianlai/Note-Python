# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #minvalue = -sys.maxsize - 1
        #maxvalue = sys.maxsize
        minvalue = -float('inf')
        maxvalue = float('inf')
        return self.helper(root, minvalue, maxvalue)
    def helper(self, node, minvalue, maxvalue):
        if not node:
            return True
        if minvalue <= node.val <= maxvalue:
            right = self.helper(node.right, node.val+1, maxvalue)
            left  = self.helper(node.left,  minvalue, node.val-1)
            #if right == left == True:
            return right and left
        else:
            return False