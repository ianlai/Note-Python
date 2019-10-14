# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, node: TreeNode) -> int:
        if node is None:
            return 0 
        
        ans = [0]  # ans[0]
        node_val_str = str(node.val)
        
        if not node.right and not node.left:
            ans = [node.val]
        
        elif node.left is None and node.right:
            self.helper(node.right, node_val_str, ans)
            
        elif node.right is None and node.left:
            self.helper(node.left,  node_val_str, ans)
        
        elif node.right and node.left:
            self.helper(node.left,  node_val_str, ans)
            self.helper(node.right, node_val_str, ans)
            
        return ans[0]
    
    def helper(self, node, cur, ans):
        if node.left is None and node.right is None:
            cur += str(node.val)            
            sum = int(cur)
            ans[0] += sum 
            return
        
        node_val_str = str(node.val)
        if node.left is None:
            self.helper(node.right, cur + node_val_str, ans)
            
        if node.right is None:
            self.helper(node.left,  cur + node_val_str, ans)
        
        if node.right and node.left:
            self.helper(node.left,  cur + node_val_str, ans)
            self.helper(node.right, cur + node_val_str, ans)
        
        return 