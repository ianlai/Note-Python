# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Traverse once [O(n), 46%]
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        p0, p1, p2 = dummy, head, head.next
        
        while p2:
            
            # p0, p1, p2 are adjacent 
            if p0.next == p1 and p1.next == p2:
                if p1.val == p2.val:
                    p2 = p2.next
                else:
                    # 3 pointers move forward together
                    p0 = p0.next
                    p1 = p1.next
                    p2 = p2.next
            else:
                if p1.val == p2.val:
                    p2 = p2.next
                else:
                    # Skip duplicate numbers
                    p0.next = p2
                    p1 = p2
                    p2 = p2.next
                    
        if p1.next and p1.val == p1.next.val: #Final skip if p1 is not pointing to the tail
            p0.next = None
            
        return dummy.next