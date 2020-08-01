# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Practice-2 (2020.08.01)
    # Since one test case, [] 0 is False, we can only traverse to leaf (not to None)
    # Therefore, the end condition is "no left and no right", and return "sum == node.val" not "sum == 0"
    # [O(n), 79%]
    def hasPathSum(self, node: TreeNode, sum: int) -> bool:
        #print("2")
        if not node:
            return False

        # print(node.val, sum)
        if not node.left and not node.right:
            return sum == node.val
            
        if node.left and self.hasPathSum(node.left, sum - node.val):
            return True
        
        if node.right and self.hasPathSum(node.right, sum - node.val):
            return True
        
        return False
        
    # =======================================================
    
    # Practice-1 (2019.10.05)
    def hasPathSum1(self, node: TreeNode, sum: int) -> bool:
        print("1")
        if node is None:
            return False
        sum -= node.val
        if node.left is None and node.right is None: 
            if sum == 0:
                return True
            else:
                return False
        if node.left is None:
            return self.hasPathSum1(node.right, sum)
        if node.right is None:
            return self.hasPathSum1(node.left, sum)
        return self.hasPathSum1(node.left, sum) or self.hasPathSum1(node.right, sum) 
            