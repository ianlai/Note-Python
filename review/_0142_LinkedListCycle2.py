# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Both slow and fast start from head, move 1 and 2 steps until they meet
    # slow starts from head again, fast continues with 1 steps. They will meet at entry point.
    # [Refector] [time O(n); space: O(1); 84%]
    def detectCycle(self, head: ListNode) -> ListNode:
        print("detectCycle")
        if head is None or head.next is None:
            return None
        
        slow, fast = head, head  
        
        #Detect the cycle
        while True:
            slow = slow.next       #do the move forward first
            fast = fast.next.next  #do the move forward first
            if fast is None or fast.next is None:  #no cycle
                return None
            if slow == fast:       #detect the cycle
                break
            
        #Make slow from the beginning again
        slow = head
        
        #Find the entrance
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
    
    #=========================================
    # Both slow and fast start from head, move 1 and 2 steps until they meet
    # slow starts from head again, fast continues with 1 steps. They will meet at entry point.
    def detectCycle1(self, head: ListNode) -> ListNode:
        print("detectCycle1")
        if head is None or head.next is None:
            return None
        
        slow, fast = head.next, head.next.next  #can't be head and head; otherwise they won't enter the loop
        
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