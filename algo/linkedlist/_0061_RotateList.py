# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        
        dummy = ListNode(-1) 
        dummy.next = head
        p1 = dummy 
        p2 = dummy
        p3 = dummy 
        
        # Calculate the number of list and effective k
        count = 0
        while p1.next:
            p1 = p1.next 
            count += 1
        k %= count
        print("count =", count, "k =", k)
        if k == 0:
            return head
        
        # Find new head
        p1 = dummy
        for i in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next 
            p2 = p2.next 
        p3 = p1.next  #p1 is new end, p2 is old end, p3 is new start
        
        # Make new links 
        p2.next = head
        p1.next = None
        head = p3
        
        return head