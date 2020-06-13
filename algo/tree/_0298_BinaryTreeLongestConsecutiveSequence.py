# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive (preorder traverse) [Space: O(n) for recursive stack, Time: O(n), 19%]
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = [1, 1]  #max, cur 
        self.helper(root, ans)
        return ans[0]
        
    def helper(self, node, ans):
        if not node:
            return 
        
        curConsecutive = ans[1]
        
        if node.left:
            if node.val - node.left.val == -1:
                ans[1] += 1
                ans[0] = max(ans[0], ans[1])
            else:
                ans[1] = 1 
            self.helper(node.left, ans)
        
        ans[1] = curConsecutive
        
        if node.right:
            if node.val - node.right.val == -1:
                ans[1] += 1
                ans[0] = max(ans[0], ans[1])
            else:
                ans[1] = 1 
            self.helper(node.right, ans)
        return 