# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Method1: Half Divide and Conquer 
    # Time Complexity = log(n) * log(n)
    def countNodes(self, root: TreeNode) -> int:
        count = 1
        if root is None: 
            return 0

        leftHight = self.getDepth(root.left)    #log(n)
        rightHight = self.getDepth(root.right)  #log(n)
        
        if leftHight == rightHight: #left is a full tree
            count += self.countNodes(root.right)
            count += pow(2, leftHight) - 1 
        else:                       #right is a full tree
            count += self.countNodes(root.left)
            count += pow(2, rightHight) - 1
        return count 
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)  #complete tree 
    
    # Method2: Divide and Conquer 
    # Time Complexity = n
    def countNodes2(self, root: TreeNode) -> int:
        count = 1
        if root is None: 
            return 0
        count += self.countNodes(root.right) 
        count += self.countNodes(root.left) 
        return count 