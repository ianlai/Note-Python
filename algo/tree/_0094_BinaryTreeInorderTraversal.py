# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    #Leetcode (best)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []    #array
        stack = []  #stack 
        
        cur = root
        while stack or cur:  #stack is empty in the first step
            #add left until reach the end
            while cur:
                stack.append(cur)
                cur = cur.left
            #get one to use
            cur = stack.pop()
            res.append(cur.val)
            
            #go right 
            cur = cur.right
        return res 
    
    #Jiuzhang (hard to understand)
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []    #array
        stack = []  #stack 
        
        dummy = TreeNode(0)
        dummy.right = root
        stack.append(dummy)
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right: 
                cur = cur.right 
                while cur:
                    stack.append(cur)
                    cur = cur.left
            if not stack:
                break
        return res[1:]  #remove dummy 
    
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []    #array
        stack = []  #stack 
        
        cur = root 
        stack.append(root)
        while stack:
            if cur.left:
                stack.append(cur.left)
                cur = cur.left         #the left bottom node will be in the right (outmost) of stack (LEFT)
            else:
                out = stack.pop()  
                res.append(out.val)    #use the node (CENTER)
                if out.right:          #(RIGHT)
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
    
        