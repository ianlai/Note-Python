# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2 types of traverse along the path: 
    # (1) normal 
    # (2) delete 
    # 
    # Deleted node means <1> its parent should link to None 
    #                    <2> children nodes will form new trees 
    
    # =======================================================================
    
    # Passing downward (argument) and upward (return) [58%]
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        print("Return as subtrees")
        if not root:
            return []
        res = []
        self.traverse(root, to_delete, res, parent_exist=False)           #start a new tree
        return res
        
    def traverse(self, root, to_delete, res, parent_exist):
        if not root:
            return 
        if root.val in to_delete:
            self.traverse(root.left, to_delete, res, parent_exist=False)  #start a new tree
            self.traverse(root.right, to_delete, res, parent_exist=False) #start a new tree
            return None #delete this node means the parent links to None  #<1>  
        else:
            if not parent_exist:
                res.append(root)  #<2> 
            root.left = self.traverse(root.left, to_delete, res, parent_exist=True)   #<1>
            root.right = self.traverse(root.right, to_delete, res, parent_exist=True) #<1>
            return root
    
    # =======================================================================
    #
    # WRONG! 
    # Originally I thought to start the traversal from sub-layer (left, right) so that we can have parent and children at the same time
    # But I should've use the return value to link the children back to parents
    # 
    def delNodes1(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        ans = []
        self.traverse(root, to_delete, ans, True)
        
        # if root.val in to_delete:
        #     if root.left and root.left.val not in to_delete:
        #         ans.append(root.left)
        #     if root.right and root.right.val not in to_delete:
        #         ans.append(root.right)
        #     self.traverse(root.left, to_delete, ans)
        #     self.traverse(root.right, to_delete, ans)
        # else:
        #     ans.append(root)
        #     self.traverse(root, to_delete, ans)
            
        return ans
        
    def traverse1(self, root, to_delete, ans, isNew):
        if not root:
            return 
        print(root.val)
        
        if isNew:
            ans.append(root)
        
        if root.left and root.left.val in to_delete:
            print("root.left", root.left.val)
            # if root.left.left and root.left.left.val not in to_delete:
            #     ans.append(root.left.left)
            # if root.left.right and root.left.right.val not in to_delete:
            #     ans.append(root.left.right)
            self.traverse(root.left.left, to_delete, ans, True)
            self.traverse(root.left.right, to_delete, ans, True)
            root.left = None
            
        elif root.right and root.right.val in to_delete:
            print("root.right", root.right.val)
            # if root.right.left and root.right.left.val not in to_delete:
            #     ans.append(root.right.left)
            # if root.right.right and root.right.right.val not in to_delete:
            #     ans.append(root.right.right)
            self.traverse(root.right.left, to_delete, ans, True)
            self.traverse(root.right.right, to_delete, ans, True)
            root.right = None
        
        
        self.traverse(root.left, to_delete, ans, False)
        self.traverse(root.right, to_delete, ans, False)
        