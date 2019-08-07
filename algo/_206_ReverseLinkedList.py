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

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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

