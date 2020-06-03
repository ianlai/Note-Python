# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class List(object):
    def __init__(self, root=None):
        self.root = root
    def init_from_list(self, mlist):
        if mlist:
            self.root = ListNode(mlist[0])
            cur = self.root
            for i in range(1, len(mlist)):
                node = ListNode(mlist[i])
                cur.next = node
                cur = node
    def traverse(self):
        cur = self.root
        while cur:
            print(str(cur.val) + " -> ", end = '') 
            cur = cur.next

class Solution:
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
     #==================================================
    def reverseList1(self, head: ListNode) -> ListNode:
        print("reverseList1")
        if not head:
            return head
        
        p1 = None 
        p2 = head
        p3 = head.next
        
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3 
            p3 = p3.next if p3 else p3 
        return p1
    
    #==================================================
    def reverseList2(self, head: ListNode) -> ListNode:
        print("reverseList2")
        if not head:
            return head
        
        p1 = None 
        p2 = head
        p3 = head.next
        
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3 
            if p3:
                p3 = p3.next
        return p1


sol = Solution()
l1 = List(ListNode())

l1.init_from_list([1,2,3,4,5])
print()
print("l1:")
l1.traverse()

l2 = List(sol.reverseList(l1.root))
print("l2:")
l2.traverse()

