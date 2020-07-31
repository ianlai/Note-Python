# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Practice 3 (2020.07.31)
    # Iterative (BFS)  [O(n), 95%]
    def isSymmetric(self, root: TreeNode) -> bool:
        print("3")
        if not root:
            return True
        queue = collections.deque([root.left, root.right])
        while queue:
            n1 = queue.popleft()
            n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            queue.append(n1.left) 
            queue.append(n2.right) 
            
            queue.append(n1.right) 
            queue.append(n2.left)
        return True
        
    #================================================

    # Practice 2 (2020.07.31)
    # Recursive (DFS), make helper function to have 2 args [O(n), 86%]
    def isSymmetric2(self, root: TreeNode) -> bool:
        print("2")
        if not root:
            return True
        return self.helper2(root.left, root.right)
    
    def helper2(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False

        if left.val != right.val:
            return False
        
        return self.helper2(left.left, right.right) and self.helper2(left.right, right.left)
          
    #================================================
    
    def isSymmetric1(self, root: TreeNode) -> bool:
        print("1")
        if not root:
            return True
        if not self.helper1(root.left, root.right):
            return False
        return True
    def helper1(self, left, right) -> bool:
        # both null
        if not left and not right: 
            return True
        # right null
        if left and not right: 
            return False
        # left null
        if not left and right: 
            return False
        # both not null
        print(left.val, right.val)
        if left.val == right.val:       
            if not self.helper1(left.left, right.right):
                return False
            if not self.helper1(left.right, right.left):
                return False
            return True
        else:
            return False
        
