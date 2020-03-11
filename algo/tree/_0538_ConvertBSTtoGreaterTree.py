# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    # Inorder traversal from right 
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)   #right first! 
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)    #left last! 
        return root
    
    #==========================================================
    # Naive solution: Get sum, preorder traversal, sum minus the subsum to be the new values 
    def convertBST2(self, root: TreeNode) -> TreeNode:
        
        cur = root 
        sum = self.sumOfTree(cur)
        #print(sum)
        
        cur = root
        self.preorder(cur, sum, [])
        
        return root 
    
    def sumOfTree(self, cur: TreeNode) -> int:
        if not cur: 
            return 0
        return self.sumOfTree(cur.left) + self.sumOfTree(cur.right) + cur.val

    def preorder(self, cur, sum, arr):
        if not cur: 
            return
        
        self.preorder(cur.left, sum, arr)
        #print("cur:", cur.val, arr)
        old_val = cur.val
        if len(arr) == 0:
            cur.val = sum
            #print(" new cur:", cur.val)
        if len(arr) >= 1: 
            cur.val = sum - arr[-1]
            #print(" new cur:", cur.val)
            
        if arr:
            arr.append(old_val + arr[-1])
        else:
            arr.append(old_val)
        self.preorder(cur.right, sum, arr)
        
        return
        
        