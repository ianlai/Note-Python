# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = [0, float('inf')]  #node.val, diff
        self.helper(root, target, ans)
        return ans[0]
        
    def helper(self, root, target, ans):
        if not root:
            return 
        
        curDiff = abs(target - root.val)
        if curDiff < ans[1]:
            ans[1] = curDiff
            ans[0] = root.val
        
        if target == root.val:
            return root.val
        elif target > root.val:
            self.helper(root.right, target, ans)
        else:
            self.helper(root.left, target, ans)