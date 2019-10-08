from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []    #array
        stack = []  #stack 
        
        cur = root 
        stack.append(root)
        while stack:
            if cur.left:
                stack.append(cur.left)
                cur = cur.left
            else:
                out = stack.pop()  
                res.append(out.val)    #use the node
                if out.right:
                    cur = out.right
                    stack.append(cur)
        return res
            
    #================================================
    
    def inorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        arr = []
        self.helper(root, arr)
        return arr
    
    def helper(self, node: TreeNode, arr: List[int]):
        if node is None:
            return 
        self.helper(node.left, arr)
        arr.append(node.val)
        self.helper(node.right, arr)
        return 
    
        