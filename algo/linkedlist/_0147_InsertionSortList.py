# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Start checking inner only when meeting a drop: while - if - while (70%)
    def insertionSortList(self, head):

        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val: #head.next val drops; needs to insert betwen start to head
                # (1) Locate nodeToInsert.
                nodeToInsert = head.next
                
                # (2) Locate nodeToInsertPre (start); insert between nodeToInsertPre and nodeToInsertPre.next
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                
                # (3) head connects to head.next.next, skip head.next (nodeToInsert)
                head.next = nodeToInsert.next
                
                # (4) Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
            
        return dummyHead.next
    
    # Naive implementation: while - while - if, without debug log (super slow: 5%)
    def insertionSortList1(self, head: ListNode) -> ListNode:    
        def insert(outer, inner):
            cur = outer.next             #moving node
            outer.next = outer.next.next #skip moving node
            cur.next = inner.next 
            inner.next = cur
            
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head 
        outer = head  #outer.next starts from 1 
        count = 1
        while outer.next != None:
            inner = dummy #inner.next starts from 0 (head) 
            isProceedInside = False
            while inner.next != outer.next:
                if outer.next.val <= inner.next.val:
                    isProceedInside = True
                    new_out_next = outer.next.next 
                    new_out = outer.next 
                    insert(outer, inner)
                    
                    #make outer and outer.next point to the next round positions
                    outer = new_out
                    while outer.next != new_out_next:
                        outer = outer.next
                    break
                else:
                    inner = inner.next
            if not isProceedInside:     
                outer = outer.next
            count += 1
        return dummy.next
    
    
    # Naive implementation, with debug log (super slow: 5%)
    def insertionSortList2(self, head: ListNode) -> ListNode:
        def traverse(head):
            cur = head
            while cur != None:
                print(str(cur.val) + " -> ", end = "")
                cur = cur.next
            print()
            return 
        
        def insert(outer, inner):
            #print("insert ", outer.next.val, " after ", inner.val)
            cur = outer.next             #moving node
            outer.next = outer.next.next #skip moving node
            cur.next = inner.next 
            inner.next = cur
            
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head 
        outer = head  #outer.next starts from 1 
        count = 1
        while outer.next != None:
            #print("[count] ", count)
            #traverse(dummy)
            
            #print("out:", outer.val, " out.next:", outer.next.val)
            inner = dummy #inner.next starts from 0 (head) 
            isProceedInside = False
            while inner.next != outer.next:
                #print("  >> in:", inner.val, "  >> in.next:", inner.next.val)
                if outer.next.val <= inner.next.val:
                    isProceedInside = True
                    new_out_next = outer.next.next 
                    new_out = outer.next 
                    #print("  >> new out: ", new_out.val, " >> new out next:", new_out_next.val)
                    insert(outer, inner)
                    
                    #make outer and outer.next point to the next round positions
                    outer = new_out
                    #print("  >>>> outer: ", outer.val, " >>>> outer next:", outer.next.val)
                    while outer.next != new_out_next:
                        outer = outer.next
                    #print("  >>>> outer: ", outer.val, " >>>> outer next:", outer.next.val)
                    break
                else:
                    inner = inner.next
            if not isProceedInside:     
                outer = outer.next
            count += 1
        return dummy.next