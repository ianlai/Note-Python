# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        ans = ListNode(0)
        cur = ans
        carry = 0 
        sum = 0 
        while True:
            if l1: 
                sum += l1.val
            if l2: 
                sum += l2.val
            if carry:
                sum += carry
                
            if sum > 9:
                carry = 1 
                cur.val = sum % 10
            else:
                carry = 0
                cur.val = sum
            
            if l1:
                print(l1.val)
                l1 = l1.next
            if l2:
                print(l2.val)
                l2 = l2.next
                
            #print(sum, "carry=", carry)
            sum = 0
            if not l1 and not l2 and not carry:
                return ans
            cur.next = ListNode(0)
            cur = cur.next
        
            