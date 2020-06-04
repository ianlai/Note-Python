# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # When finding a target, we always remove it from the original list and add it to the new list 
    # (not combine the actions) [O(n), 80%]
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        p1, p2 = dummy, head
        headLarge = None
        isFirstLarge = True
        
        while p2.next:
            if p2.val >= x:
                
                #Create new list 
                if isFirstLarge:
                    headLarge = p2
                    tailLarge = p2
                    isFirstLarge = False
                
                p1.next = p2.next
                p3 = p2
                p2 = p2.next
                
                #List 2
                p3.next = None
                if tailLarge != p3: #otherwise, it might create a loop
                    tailLarge.next = p3
                    tailLarge = tailLarge.next
            else:
                if p1.next != p2:
                    p1.next = p2 

                p1 = p1.next
                p2 = p2.next
        
        #Check whether the new list is created 
        if not headLarge:
            return dummy.next 
        
        #Handle the last element
        if p2.val >= x:
            tailLarge.next = p2
            p1.next = headLarge
        else:
            p2.next = headLarge
            
        return dummy.next
        