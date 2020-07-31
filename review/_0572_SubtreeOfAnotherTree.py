# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    # Practice 2 (2020.07.31)
    # Recursive [O(n), 70%]
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        print("Practice 2")
        def isSame(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            else:
                return isSame(s.left, t.left) and isSame(s.right, t.right)
                
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        if isSame(s, t): #We can't use s.val == t.val (not enough) 
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) #If not the same, we need to go deeper
    
    #=======================================================
    
    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        print("Practice 1")
        if not s and not t:
            return True
        if not s:
            return False
        
        if self.isMatch1(s, t):
            return True
        else:
            return self.isSubtree1(s.left, t) or self.isSubtree1(s.right, t)
            
    def isMatch1(self, s, t) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isMatch1(s.left, t.left) and self.isMatch1(s.right, t.right) 