# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 2 layer DFS [O(n2), 36%]
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        count = [0]
        self.dfs(root, sum, count)
        return count[0]
        
    def dfs(self, root, sum, count):
        if not root:
            return 
        ###print("dfs:", root.val)
        
        self.sumDown(root, sum-root.val, count)
        # self.sumDown(root.left, sum-root.val, count)
        # self.sumDown(root.right, sum-root.val, count)
        
        self.dfs(root.left, sum, count)
        self.dfs(root.right, sum, count)        
        
    def sumDown(self, root, sum, count):
        if not root:
            return 
        ###print("  sumDown:", root.val, sum)
        
        #if not root.left and not root.right:  #NO, we don't only count until reaching the leaves 
        if sum == 0:
            count[0] += 1
        
        if root.left:
            self.sumDown(root.left, sum-root.left.val, count)
        if root.right:
            self.sumDown(root.right, sum-root.right.val, count)
            
            
            