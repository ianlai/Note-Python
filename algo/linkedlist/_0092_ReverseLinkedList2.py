# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #Use dummy node; separate to 3 steps [O(n), 82%]
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(None)  #dummy node is necessary (especially when m == 1)
        dummy.next = head
        
        # (1) Reach the point to start reverse
        p0, p1 = dummy, head
        count = 0
        for count in range(m-1):
            p0 = p0.next   #p0 points to last of segment-1
            p1 = p1.next   #p1 points to first of segment-2 (before reverse)
            
        if not p0 or not p1:
            return head
        
        # (2) Reverse 
        d1, d2, d3 = None, p1, p1.next
        count = 0
        for count in range(n-m+1):
            if d2:
                d2.next = d1
                d1 = d2 
                d2 = d3    #d1 points to last of segment-2 (before reverse)
                if d3:
                    d3 = d3.next  #d2 points to first of segment-3
        
        # (3) Connect segment-1's tail to segment-2's head; coonnect segment-2'tail to segment-3's head
        p0.next = d1
        p1.next = d2 

        return dummy.next