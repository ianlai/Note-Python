# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #HashSet; space: O(n) 
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        s = set()
        ptr = head
        while ptr != None:
            if ptr in s:
                return True
            else:
                s.add(ptr)
                ptr = ptr.next
        return False
        
    #Slow, fast pointer; space: O(1)
    def hasCycle2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast: 
            #print(slow.val, fast.val)
            if fast.next == None or fast.next.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True
                    
        
        
            