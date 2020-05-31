# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Leave loop when either l1 or l2 ends (refactored) [O(min(M, N), 71%-99%]
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy 
        
        # Only deal with the case which needs comparison 
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next 
            else:
                cur.next = l2
                l2 = l2.next 
            cur = cur.next 
        # The remaining list can be handled with if clauses
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next
    
    #================================================================

    # Leave loop when either l1 or l2 ends [O(min(M, N), 71%-99%]
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Special cases
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        cur = dummy 
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                cur.next = l2 
                break
            if l2 is None:
                cur.next = l1
                break
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next 
                    l1 = l1.next 
                else:
                    cur.next = l2
                    cur = cur.next 
                    l2 = l2.next 
        return dummy.next
    
    #================================================================
    
    # Traverse both list [O(N+M), 45%-71%]
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Special cases
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        cur = dummy 
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                cur.next = l2 
                cur = cur.next 
                l2 = l2.next
                continue      #necessary 
            if l2 is None:
                cur.next = l1
                cur = cur.next 
                l1 = l1.next 
                continue      #necessary 
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next 
                    l1 = l1.next 
                else:
                    cur.next = l2
                    cur = cur.next 
                    l2 = l2.next 
        return dummy.next