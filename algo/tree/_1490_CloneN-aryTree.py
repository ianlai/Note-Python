"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    
    # Remember to use return [O(N), 46%]
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        res = Node(root.val)
        
        for node in root.children:
            newNode = self.cloneTree(node)
            res.children.append(newNode)
            
        return res
        
            