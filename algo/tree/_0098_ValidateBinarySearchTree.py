# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST_traverse(root)
        
    ### Traverse 
    def isValidBST_traverse(self, root: TreeNode) -> bool:
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
    
    ### Divide and Conquer 
    def isValidBST_dnc(self, root: TreeNode) -> bool:
        #minvalue = -sys.maxsize - 1
        #maxvalue = sys.maxsize
        minvalue = -float('inf')
        maxvalue = float('inf')
        return self.helper(root, minvalue, maxvalue)
    def helper(self, node, minvalue, maxvalue):
        if not node:
            return True
        if minvalue <= node.val <= maxvalue:
            right = self.helper(node.right, node.val+1, maxvalue)
            left  = self.helper(node.left,  minvalue, node.val-1)
            #if right == left == True:
            return right and left
        else:
            return False