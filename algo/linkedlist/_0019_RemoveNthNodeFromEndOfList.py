# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        left, right = dummy, dummy
        
        #step1 - find nth node
        for i in range(n):
            right = right.next 
        
        #step2 - fine nth node from the tail (one before)
        while right.next is not None:
            left = left.next
            right = right.next
        
        #step3 - delete
        left.next = left.next.next
        
        return dummy.next