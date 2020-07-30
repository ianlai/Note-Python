# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Traverse and store in an ascending array [O(n), 28%]
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        arr = []
        self.inorder(root, p, arr)
        
        for i in range(len(arr)):
            if arr[i].val == p.val and i < len(arr) - 1:
                return arr[i+1]
        return None
        
    def inorder(self, root, p, arr):
        if not root:
            return None
        
        self.inorder(root.left, p, arr)
        arr.append(root)
        # if root.val == p.val:  #Can't add this otherwise, we can't find the target if it's in right subtree
        #     return 
        self.inorder(root.right, p, arr)
            
    #=============================================================
        
    # Wrong (traverse but return)
    def inorderSuccessor1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        print("Wrong")
        if not root:
            return None
        
        left = self.inorderSuccessor(root.left, p)
        if not left:
            return None
        else:
            return left
        
        if root.val == p.val:
            return self.inorderSuccessor(root.right, p)
        
        right = self.inorderSuccessor(root.right, p)
            
        if not right:
            return None
        else:
            return right
        
        