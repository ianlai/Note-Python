# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head and not head.next:
            return head
        if head and head.next:
            #print(head.val, " ")
            next_pair = head.next.next
            new_head = head.next
            head.next.next = head
            head.next = self.swapPairs(next_pair)
            return new_head
        
        