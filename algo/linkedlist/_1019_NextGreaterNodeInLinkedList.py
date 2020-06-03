# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    # Backward traverse, stack stores integer [O(n), 52%]
    def nextLargerNodes1(self, head: ListNode) -> List[int]:
        print("Backward traverse, stack stores integers")
        if not head:
            return []
        
        index = 0
        cur = head
        
        A, B = [], []
        ans = []
        
        # Traverse 
        while cur != None:
            ans.append(0)
            A.append(cur.val)
            cur = cur.next
        
        # Backward traverse 
        for i in range(len(A)-1, -1, -1):
            cur = A.pop()
            while B and B[-1] <= cur:
                B.pop()
                
            if not B:
                B.append(cur)
                continue
                
            ans[i] = B[-1] 
            B.append(cur)
            
        return ans 
    
    #========================================================
    
    # Forward traverse, stack stores tuple [O(n), 36%]
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        print("Forward traverse, stack stores tuple")
        if not head:
            return []
        
        index = 0
        cur = head
        stack = [(head.val, index)]
        ans = []
        
        while cur != None:
            ans.append(0)
            
            while stack and cur.val > stack[-1][0]:
                popped = stack.pop()
                ans[popped[1]] = cur.val
                
            if (not stack) or (stack and cur.val <= stack[-1][0]):
                stack.append((cur.val, index))
                
                stack.append((cur.val, index))
            
            cur = cur.next
            index += 1 
        
        return ans