# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Slow and fast pointers [space:O(1), 39%-91%]
    def middleNode(self, head: ListNode) -> ListNode:
        print("two pointers")
        if not head or not head.next:
            return head
        
        slow, fast = head, head 
        while not (not fast.next or not fast.next.next):
            slow = slow.next
            fast = fast.next.next
            
        if not fast.next: 
            return slow
        else:
            return slow.next
    #================================================
    
    # Output to an array [space:O(n), 71%]
    def middleNode1(self, head: ListNode) -> ListNode:
        print("array")
        arr = []
        while head != None:
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]


