# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        
        #In-order traverse 
        arr = []
        self.traverse(root, arr)  #in-order

        #Two sum
        i, j = 0, len(arr) - 1
        while i < j:
            sum = arr[i] + arr[j]
            if sum > k: 
                j -= 1
            elif sum < k :
                i += 1
            else:
                return True
            
        return False
    def traverse(self, node, arr):
        if node is None:
            return 
        
        self.traverse(node.left, arr)
        arr.append(node.val)
        self.traverse(node.right, arr)
        
        return 