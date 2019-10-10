"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    
    # node.children is a treenode list 
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return None
        
        ans = []
        cur_layer_arr = []
        next_layer_arr = []
        
        cur_layer_arr.append(root)
        
        while cur_layer_arr:
            for node in cur_layer_arr:
                next_layer_arr.extend(node.children) #append a list into an existing list
                
            if cur_layer_arr:
                ans.append([x.val for x in cur_layer_arr])
            cur_layer_arr = next_layer_arr #reuse: set cur_layer to be next_layer
            next_layer_arr = []            #reuse: clear next_layer
            
        return ans
            
            
            
        