"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        return self.helper(root)
    
    def helper(self, node):
        if not node:
            return 0
        
        maxDepth = 0
        for child in node.children:
            maxDepth = max(maxDepth, self.helper(child))
        return 1 + maxDepth