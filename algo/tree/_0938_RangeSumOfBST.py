# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Divide and Conquer (30%)
    def rangeSumBST_DC(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        sum_left  = self.rangeSumBST(root.left, L, R)
        sum_right = self.rangeSumBST(root.right, L, R)
        
        sum = sum_left + sum_right
        if L <= root.val <= R:
            return sum + root.val
        else:
            return sum 
    
    # In-order Traversal (50%) 
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        cur = root 
        sum = 0 
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            value = cur.val     #get this value 
            
            # if over R then return (40% -> 50%)
            if value > R:
                break 
            if value < L:
                cur = cur.right
                continue
            sum += value
            cur = cur.right 
        return sum