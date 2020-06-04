# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Traverse once, handle the cases with odd number or even number nodes [O(n), 73%-96%]
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        headEven = head.next
        prevOdd = head
        
        while not (not odd or not even):
            if odd.next == even:
                odd.next = even.next
                prevOdd = odd  #keep the last odd 
                odd = odd.next
            else:
                even.next = odd.next
                even = even.next
                 
        if odd:   #odd number of nodes 
            odd.next = headEven 
        else:     #even number of nodes
            prevOdd.next = headEven
        return head