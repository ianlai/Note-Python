"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        #Corner case
        if not node:
            return node
        
        #Initialize
        node_map = {}
        
        #BFS
        node_set = self.bfs(node)              #traverse the old set (no duplication)
        
        #Copy nodes
        for old_node in node_set:
            new_node = Node(old_node.val, [])  # new node should have no neighbor when initialized 
            node_map[old_node] = new_node      # new graph is stored at node_map

        #Copy edges 
        for old_node in node_set:
            for old_neighbor in old_node.neighbors:
                new_neighbor = node_map[old_neighbor]
                node_map[old_node].neighbors.append(new_neighbor)
                
        return node_map[node]
    
    def bfs(self, node):
        node_queue = deque([node])
        node_set = set([])
        while node_queue:
            cur = node_queue.popleft()
            if cur in node_set:
                continue
            node_set.add(cur)
            for neighbor in cur.neighbors:
                node_queue.append(neighbor)
        return node_set