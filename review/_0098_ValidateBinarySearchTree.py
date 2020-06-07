# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    # Inorder Traversal [space: O(1), time: O(n), 47%]
    def isValidBST1(self, root: TreeNode) -> bool:
        print("Inorder Traversal")
        
        arr = []
        self.traverse(root, arr)
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False
        return True
    
    def traverse(self, node, arr):
        if not node:
            return 
        self.traverse(node.left, arr)
        arr.append(node.val)
        self.traverse(node.right, arr)
        return
  
    #================================================
    
    # Divide and Conquer (refactor) [space stack: O(logn), time:O(n), 71%]
    # Faster than D&C without refactor because now we will return False if right sub-tree returns false 
    def isValidBST(self, root: TreeNode) -> bool:
        print("Divide and Conquer (refactor)")
        minvalue = -float('inf')
        maxvalue = float('inf')
        return self.helper(root, minvalue, maxvalue)
    def helper(self, node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        if not self.helper(node.right, node.val, high):
            return False
        if not self.helper(node.left,  low, node.val):
            return False
        return True
        
    #================================================
    
    # Divide and Conquer [space stack: O(logn), time: O(n), 47%]
    def isValidBST2(self, root: TreeNode) -> bool:
        print("Divide and Conquer")
        minvalue = -float('inf')
        maxvalue = float('inf')
        return self.helper(root, minvalue, maxvalue)
    def helper(self, node, minvalue, maxvalue):
        if not node:
            return True
        if minvalue <= node.val <= maxvalue:
            isRight = self.helper(node.right, node.val+1, maxvalue) 
            isLeft  = self.helper(node.left,  minvalue, node.val-1)
            return isRight and isLeft
        else:
            return False