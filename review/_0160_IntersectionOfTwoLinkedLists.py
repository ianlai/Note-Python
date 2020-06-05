# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Make the A's tail connect to B to form a cycle (if has an intersection) or a long list (if no intersection)
    # Find the cycle entry and recover the modified linked lists (MUST) [44%]
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        #Find the end
        ptrA = headA
        while ptrA.next != None:
            ptrA = ptrA.next
        
        #Connect end to headB (to form a cycle or long list)
        ptrA.next = headB 
        
        #Make slow and fast meet 
        slow, fast = headA, headA
        while True:
            slow = slow.next
            fast = fast.next.next
            if fast is None or fast.next is None:
                ptrA.next = None   #Recover the linkedlist B
                return None            
            if slow == fast:
                break 
            
        #Find the entrance
        ptr1, ptr2 = headA, fast
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        #Recover the linkedlist B
        ptrA.next = None 
        
        return ptr1
        