# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Separate to 3 functions: findMiddle, reverse, merge [O(n), 85%] [28min]
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        middle = self.findMiddle(head) #return first if even; return middle if odd
        head2 = middle.next
        middle.next = None 
        
        # print("After findMiddle")
        # self.printList(head)
        # self.printList(head2)
        
        head2 = self.reverse(head2)
        
        # print("After reverse")
        # self.printList(head)
        # self.printList(head2)
        
        head = self.merge(head, head2)
        
        # print("After merge")
        # self.printList(head)
        # self.printList(head2)
        
        return head 
    
    def findMiddle(self, head):
        slow, fast = head, head
        
        while not(not fast or not fast.next or not fast.next.next):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        p1, p2, p3 = None, head, head.next
        while p2: 
            p2.next = p1
            p1 = p2 
            p2 = p3
            if p3:
                p3 = p3.next
        return p1
    
    def merge(self, head1, head2):
        p11, p12, p21, p22 = head1, head1.next, head2, head2.next
        
        while p12:
            p11.next = p21
            p21.next = p12
            p11 = p12
            p12 = p12.next
            p21 = p22
            if p22:
                p22 = p22.next
        if p21:
            p11.next = p21
            
        return head1
    
    def printList(self, head):
        p1 = head
        while p1:
            print(p1.val, "->", end="")
            p1 = p1.next
        print()
      