# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Merge sort (compare 2 groups) [O(nlogn), 31%]
    def sortList(self, head: ListNode) -> ListNode:
        #print("Merge sort")
        if not head or not head.next: # 0 or 1 
            return head
        
        #(1) Separate the list to be two 
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
    
        rightHead = slow.next 
        leftHead = head 
        slow.next = None #cut the tail 
        
        # self.printList(leftHead)
        # self.printList(rightHead)
        
        #(2) Recursively separate the lists 
        rightHead = self.sortList(rightHead)
        leftHead = self.sortList(leftHead)
        
        #(3) Merge the two lists
        head = self.merge(leftHead, rightHead)
        return head
    
    def merge(self, l1, l2):
        dummy = ListNode(None)
        cur = dummy  
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next
            
    #======================================================
    
    # Insertion sort (compare one by one) [O(n2), TLE]
    def sortList1(self, head: ListNode) -> ListNode:
        print("Insertion sort")
        if not head or not head.next:
            return head
        
        newList = ListNode(None) #new list 
        cur = head
        
        while cur:
            nextNode = cur.next
            cur.next = None  #cut one node
            newList.next = self.mergeTwoLists(newList.next, cur) #merge the cutted node to the new list
            cur = nextNode
        return newList.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy 
        
        # Only deal with the case which needs comparison 
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next 
                l1 = l1.next 
            else:
                cur.next = l2
                cur = cur.next 
                l2 = l2.next 
        # The remaining list can be handled with if clauses
        if l1 is None:
            cur.next = l2 
        elif l2 is None:
            cur.next = l1
        return dummy.next
    
    def printList(self, l):
        while l != None:
            print(l.val, "->", end =" ")
            l = l.next
        print()
        return 
    