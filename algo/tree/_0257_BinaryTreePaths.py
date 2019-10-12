# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        ans = []
        cur = str(root.val)
        if root.left:
            self.helper(root.left, ans, cur) 
        if root.right:
            self.helper(root.right, ans, cur)
        if not root.left and not root.right:
            ans.append(cur)
        return ans
        
    def helper(self, node, ans, cur):
        cur += "->" + str(node.val)
        if not node.left and not node.right: #both leaf need to be None, so we end one layer earlier
            ans.append(cur)
            return 
        if node.left:
            self.helper(node.left, ans, cur)
        if node.right:
            self.helper(node.right, ans, cur)
        return 