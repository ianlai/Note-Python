"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    
    #Iterative (Stack) [41%]
    def preorder(self, root: 'Node') -> List[int]:
        print("Iterative (Stack)")
        if not root:
            return []
        
        stack = [root]
        ans = []
        
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            for i in range(len(cur.children)-1, -1, -1):  #Add from right to left (reversed order)
                child = cur.children[i]
                stack.append(child)
        return ans
                
    #============================================
    
    #Recursive [12%]
    def preorder1(self, root: 'Node') -> List[int]:
        print("Recursive")
        if not root:
            return []
        
        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if not root:
            return 
        ans.append(root.val)
        for child in root.children:
            self.helper(child, ans)
        return
  
    #============================================

    #BFS (Incorrect!! BFS is using concept of queue, which doesn't fit the traversal with stack) 
    def preorder2(self, root: 'Node') -> List[int]:
        print("BFS (incorrect!!)")
        if not root:
            return []
        ans = []
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):    
                node = queue.popleft()
                ans.append(node.val)
                
                for child in node.children:
                    queue.append(child)
        return ans