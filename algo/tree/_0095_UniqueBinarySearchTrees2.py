# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive [28%]
    # => Return the list instead of passing a list to fill it 
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        
        result = self.generateSubTree(1, n)
        return result
            
    def generateSubTree(self, start, end):
        if start > end:
            return [None]
        
        subTrees = []
        for i in range(start, end+1):
            
            # leftList = []
            # rightList = []
            leftList = self.generateSubTree(start, i-1)
            rightList = self.generateSubTree(i+1, end)
            for l in leftList:
                for r in rightList:
                    #print(i)
                    root = TreeNode(i) 
                    root.left = l
                    root.right = r
                    subTrees.append(root)
        return subTrees
            