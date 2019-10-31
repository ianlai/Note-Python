# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        ans = [] 
        self.helper(root, ans, "")
        return sum(ans)
        
    def helper(self, node, ans, cur):
        if node:
            if node.left is None and node.right is None:
                cur = cur+str(node.val)
                ans.append(int(cur, 2))  #base 2 
                return 

            self.helper(node.left, ans, cur+str(node.val))
            self.helper(node.right, ans, cur+str(node.val))
         