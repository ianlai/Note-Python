# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverseListSimple(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    #==================================================
    def reverseList(self, head):
        print("reverseList0")
        if not head or not head.next: 
            return head
        
        p1, p2 = None, head
        while p2:
            p2.next, p1, p2 = p1, p2, p2.next
        return p1
     #==================================================
    def reverseList1(self, head: ListNode) -> ListNode:
        print("reverseList1")
        if not head:
            return head
        
        p1 = None 
        p2 = head
        p3 = head.next
        
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3 
            p3 = p3.next if p3 else p3 
        return p1
    
    #==================================================
    def reverseList2(self, head: ListNode) -> ListNode:
        print("reverseList2")
        if not head:
            return head
        
        p1 = None 
        p2 = head
        p3 = head.next
        
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3 
            if p3:
                p3 = p3.next
        return p1