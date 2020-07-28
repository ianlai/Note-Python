# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursive, return the current node [41%]
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        print("root:", root.val, "del:", key)
        
        if root.val == key:
            if not root.left:
                print("case1")
                return root.right
            if not root.right:
                print("case2")
                return root.left
            
            #if root.left.left and root.left.right: #left is full, choose right 
            if not root.right.left:  #easy
                print("case3")
                root.right.left = root.left 
                return root.right
            
            if not root.left.right: #easy
                print("case4")
                root.left.right = root.right
                return root.left 
            
            print("complex case - find the smallest in the right subtree")
            #newkey = root.right.left.val
            cur = root.right
            while cur.left != None:
                cur = cur.left
            newkey = cur.val
            root.val = newkey
            root.right = self.deleteNode(root.right, newkey)
            return root
            
        elif key > root.val:
            print("right")
            root.right = self.deleteNode(root.right, key)
            
        else: 
            print("left")
            root.left = self.deleteNode(root.left, key)
            
        return root