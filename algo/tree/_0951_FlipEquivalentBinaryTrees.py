# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    
    # Recursive [29%]
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        LL  = self.flipEquiv(root1.left, root2.left)
        LR  = self.flipEquiv(root1.left, root2.right)
        RL  = self.flipEquiv(root1.right, root2.left)
        RR  = self.flipEquiv(root1.right, root2.right)
        
        if LL and RR:
            return True
        if LR and RL:
            return True
        return False


#     def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
#         if not root1 or not root2:
#             return False
        
#         if root1.val != root2.val:
#             return False
#         print("me:", root1.val, root2.val)
#         return self.flipEquivNextLayer(root1, root2)
    
#     def flipEquivNextLayer(self, root1, root2):
#         if not root1 and root2:
#             return False
        
#         if not root2 and root1:
#             return False
#         print("me:", root1.val, root2.val)
# #         if not root1.left and root2.left and root2.right:
# #             return False
        
# #         if not root1.right and root2.left and root2.right:
# #             return False
        
# #         if not root2.left and root1.left and root1.right:
# #             return False
        
# #         if not root2.right and root1.left and root1.right:
# #            return False
        
        
#         #print("root1:", root1.left.val, root1.right.val, "root2:", root2.left.val, root2.right.val)
        
#         if not root1.left and not root1.right: #0
#             print("0")
#             if not root2.left and not root2.right: 
#                 return True
#             return False
        
#         if root1.left and not root1.right: #1: root1.left
#             print("1: root1.left")
#             if not root2.left and not root2.right:
#                 return False
#             if root2.left and root2.right:
#                 return False
#             if root2.right:
#                 self.flipEquivNextLayer(root1.left, root2.right)
#             if root2.left:
#                 self.flipEquivNextLayer(root1.left, root2.left)
                
#         if not root1.left and root1.right: #1: root1.right
#             print("2: root1.right")
#             if not root2.left and not root2.right:
#                 return False
#             if root2.left and root2.right:
#                 return False
#             if root2.right:
#                 self.flipEquivNextLayer(root1.right, root2.right)
#             if root2.left:
#                 self.flipEquivNextLayer(root1.right, root2.left)
        
                    
#         if root1.left and root1.right: #2
#             print("3: root1.left and root1.right")
#             if not root2.left or not root2.right:
#                 print("FFF")
#                 return False
#             if root1.left.val == root2.left.val and root1.right.val == root2.right.val:  #true
#                 if not self.flipEquivNextLayer(root1.left, root2.left):
#                     return False              
#                 if not self.flipEquivNextLayer(root1.right, root2.right):
#                     return False
#             if root1.left.val == root2.right.val and root1.right.val == root2.left.val:
#                 if not self.flipEquivNextLayer(root1.left, root2.left):
#                     return False              
#                 if not self.flipEquivNextLayer(root1.right, root2.right):
#                     return False
#             return True