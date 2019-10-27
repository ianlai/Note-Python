# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        ans = []
        deq1 = deque([root]) #current layer
        deq2 = deque()       #next layer
        
        while deq1 or deq2:
            #traverse deq1 and create deq2
            cur = None
            while deq1:
                cur = deq1.popleft()
                if cur.left:
                    deq2.append(cur.left)
                if cur.right:
                    deq2.append(cur.right)
                    
            #next layer
            deq1 = deq2 
            deq2 = deque()
            
            ans.append(cur.val)
                
        return ans