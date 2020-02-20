# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        
        slow, fast = head.next, head.next.next  #initial values are critical
        
        #detect the cycle
        while True:
            if fast is None or fast.next is None:  #no cycle
                return None
            if slow == fast:                       #found the cycle
                break
            slow = slow.next
            fast = fast.next.next
            
        #make slow from the beginning again
        slow = head
        
        #find the entrance
        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
            
        return None