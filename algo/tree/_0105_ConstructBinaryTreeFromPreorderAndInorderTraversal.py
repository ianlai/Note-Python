# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # preorder = [3,1,2,4]
    # inorder  = [1,2,3,4]
    #      3 
    #    1   4 
    #  x  2
    
    # preorder = [3,1,2,4]
    # inorder  = [2,1,3,4]
    #      3 
    #    1   4 
    #  2  x
    
    # Using slice is simple
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None 
        
        head = TreeNode(preorder[0])
        pivotIdx = inorder.index(preorder[0])
        
        head.left  = self.buildTree(preorder[1:pivotIdx+1], inorder[:pivotIdx])
        head.right = self.buildTree(preorder[pivotIdx+1:] , inorder[pivotIdx+1:])
        return head
            
     # WRONG! (using idx) 
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder) == 0:
#             return None 
#         head = TreeNode(preorder[0])
#         pivotIdx = inorder.index(head.val)
#         self.helper(preorder, inorder, head, pivotIdx, 1) 
#         return head
    
#     def helper(self, preorder, inorder, head, pivotIdx, preIdx):
#         if preIdx >= len(preorder):
#             return 
#         print()
#         print("THIS > head:", head.val, "pivotIdx:", pivotIdx)
#         nextInIdx = inorder.index(preorder[preIdx])
#         print("NEXT >> preNode:", preorder[preIdx], "preIdx:", preIdx, "nextInIdx:", nextInIdx) 
#         if nextInIdx < pivotIdx: 
#             head.left = TreeNode(preorder[preIdx])
#             print("head(", head.val, ") -> ", "left(", head.left.val,")" )
#             self.helper(preorder, inorder, head.left, nextInIdx, preIdx+1)
#         else:
#             head.right = TreeNode(preorder[preIdx])
#             print("head(", head.val, ") -> ", "right(", head.right.val,")" )
#             self.helper(preorder, inorder, head.right, nextInIdx, preIdx+1)
            