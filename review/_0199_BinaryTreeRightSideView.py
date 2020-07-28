# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    
    # BFS with one layer at a time (for loop) [O(n), 59%]
    def rightSideView(self, root: TreeNode) -> List[int]:
        print("BFS + One layer at a time")
        if not root:
            return []
        ans = []
        deq = deque([root])
        
        while deq:
            for _ in range(len(deq)):
                cur = deq.popleft()                    
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            ans.append(cur.val) #last element
                    
        return ans
                
        
    #=================================================================

    # BFS with sentinel node [O(n), 59%]
    def rightSideView2(self, root: TreeNode) -> List[int]:
        print("BFS + Sentinel node")
        if not root:
            return []
        
        ans = []
        deq = deque([root, None])
        
        nex = deq.popleft()
        while deq:
            
            cur, nex = nex, deq.popleft() #move one step forward
            
            # since "None" represents the separator now, we can't add any None node as a leaf
            if cur.left:
                deq.append(cur.left)
            if cur.right:
                deq.append(cur.right)
            
            # if reaches the end of one layer
            if not nex: 
                ans.append(cur.val)
                deq.append(None) 
                cur, nex = nex, deq.popleft() #let cur skip the sentinel node and start from the next layer
                
        return ans
            
    #=================================================================
    
    #BFS with 2 queues (get the last element in a layer) [O(n), 79%]
    def rightSideView1(self, root: TreeNode) -> List[int]:
        print("BFS + 2 Queues")
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