"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    
    # Traverse twice (separate assign value and assign random node) [time: O(n), space: O(n), 16%]
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        cur1 = head
        dummy = Node(0)
        cur2 = Node(0)
        dummy.next = cur2 
        nodeMap = {}  #Map of node in list 1 to node in list 2
        
        # (1) Create nodes in list 2 and assign the value
        while cur1.next != None:
            cur2.val = cur1.val
            cur2.next = Node(0)
            nodeMap[cur1] = cur2
            cur1 = cur1.next
            cur2 = cur2.next
        
        cur2.val = cur1.val  #last one
        nodeMap[cur1] = cur2
            
        # self.printList(head)
        # self.printList(dummy.next)
            
        cur1 = head
        cur2 = dummy.next
        
        # (2) Assign the random nodes based on the map
        while cur1 != None:
            if cur1.random:
                cur2.random = nodeMap[cur1.random]
            else:
                cur2.random = None
            cur1 = cur1.next
            cur2 = cur2.next
            
        return dummy.next
            
    def printList(self, head):
        cur = head
        while cur != None:
            print(cur.val, " -> ", end = "")
            cur = cur.next
        print()