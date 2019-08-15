# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    ### 1. Traverse (in-order)
    # def maxDepth(self, root: TreeNode) -> int:
    #     self.depth = 0 
    #     self.traverse(root, 1)
    #     return self.depth
    # def traverse(self, node, curDepth):
    #     if not node:
    #         return 
    #     self.depth = max(self.depth, curDepth)
    #     self.traverse(node.left,  curDepth+1)
    #     self.traverse(node.right, curDepth+1)
    #     return 
        
    ### 2. Divide and Conquer (concise)
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1   
    

    ### 3. Divide and Conquer (verbal)
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root: 
    #         return 0
    #     return self.helper(root, 0)
    # def helper(self, root, depth):
    #     if not root:
    #         return depth
    #     else:
    #         left_depth = self.helper(root.left, depth+1)
    #         right_depth = self.helper(root.right, depth+1)
    #         return max(left_depth, right_depth)
            