# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        #find the end
        ptrA = headA
        while ptrA.next != None:
            ptrA = ptrA.next
        
        #connect end to headB
        ptrA.next = headB 
        
        #make slow and fast meet 
        slow, fast = headA, headA
        while True:
            slow = slow.next
            fast = fast.next.next
            if fast is None or fast.next is None:
                ptrA.next = None   #recover the linkedlist B
                return None            
            if slow == fast:
                break 
            
        
        #find the entrance
        ptr1, ptr2 = headA, fast
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        #recover the linkedlist B
        ptrA.next = None 
        
        return ptr1
        