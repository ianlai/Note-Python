# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        p1 = dummy 
        p2 = head 
        
        while p2:
            #print(str(p1.val) + " " + str(p2.val))
            if p2.val == val:
                p1.next = p2.next 
                p2 = p1.next    #go 1 step 
                # p1 = p1.next  #go 2 steps but many edge cases then
                # if p1:
                #     p2 = p1.next
            else:
                p1 = p1.next 
                p2 = p2.next
                
        return dummy.next 
                
        