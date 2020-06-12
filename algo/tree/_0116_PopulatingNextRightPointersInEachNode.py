"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    # Recursive; Handle 2 Connection types (same parent, different parent)  [Space: O(1), Time: O(n), 38% - 79%]
    # Key concept is that when at layer n, we establish the connection-1 of layer n+1
    # And when traversing to layer n+1, we establish the connection-2 of layer n+1 (and connection-1 of layer n+2)
    def connect(self, root: 'Node') -> 'Node':
        print("2 Connection Types")
        if not root:
            return root
        
        self.helper(root)
        return root
    
    def helper(self, node):
        if not node:
            return
        
        if node.left:
            node.left.next = node.right      #connection-1 
        if node.next and node.right:
            node.right.next = node.next.left #connection-2
            
        self.helper(node.left)
        self.helper(node.right)

    # =========================================================    
    
    # BFS [Space: O(N) for queue, Time: O(n), 58% - 79%]
    def connect2(self, root: 'Node') -> 'Node':
        print("BFS")
        if not root:
            return root
        q = collections.deque([root])
        
        while q and q[0]:
            for idx in range(len(q)):
                if idx == 0:
                    cur = q.popleft()
                elif idx == len(q) - 1:
                    cur.next = None
                else:
                    cur.next = q.popleft()
                    cur = cur.next
                q.append(cur.left)
                q.append(cur.right)
        return root